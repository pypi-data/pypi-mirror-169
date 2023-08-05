#!/usr/bin/env python
# -*- coding: utf8 -*-
from __future__ import absolute_import, division, generators, nested_scopes, print_function, unicode_literals, with_statement

import re
import json
import yaml
import logging

from zenutils import jsonutils
from zenutils import treeutils
from magic_import import import_from_string

from django.apps import apps
from django.shortcuts import render
from django.utils.translation import gettext
from django.db import models
from django.urls import reverse
from django.urls import resolve
from django.urls import get_resolver
from django.db import models

from django_apiview.utils import get_setting_value
from django_apiview.utils import get_server_host
from django_apiview.swagger_ui.fields import get_field_type

logger = logging.getLogger(__name__)

def get_model_name(model):
    return f"{model.__module__}.{model.__name__}"

def get_model_ref(model):
    model_name = get_model_name(model)
    return f"#/definitions/{model_name}"

def get_model_definition(model):
    definition = {}
    definition["type"] = "object"
    definition["properties"] = {}
    if issubclass(model, models.Model):
        for field in model._meta.get_fields():
            field_name = field.name
            if "+" in field_name:
                continue
            definition["properties"][field_name] = {}
            definition["properties"][field_name] = get_field_type(field)
    else:
        for field_name, field in model.base_fields.items():
            definition["properties"][field_name] = {}
            definition["properties"][field_name] = get_field_type(field)
    return definition

def get_definitions():
    definitions = {}
    for app in apps.get_app_configs():
        app_module = app.module
        DJANGO_APIVIEW_SWAGGER_EXPORT_ALL_MODELS = getattr(app_module, "DJANGO_APIVIEW_SWAGGER_EXPORT_ALL_MODELS", False)
        if DJANGO_APIVIEW_SWAGGER_EXPORT_ALL_MODELS:
            for model in app.get_models():
                model_name = get_model_name(model)
                model_definition = get_model_definition(model)
                if not model_name in definitions:
                    definitions[model_name] = model_definition
        DJANGO_APIVIEW_SWAGGER_EXPORT_MODELS = getattr(app_module, "DJANGO_APIVIEW_SWAGGER_EXPORT_MODELS", [])
        for model_path in DJANGO_APIVIEW_SWAGGER_EXPORT_MODELS:
            model = import_from_string(model_path)
            if model:
                model_name = get_model_name(model)
                model_definition = get_model_definition(model)
                if not model_name in definitions:
                    definitions[model_name] = model_definition
    return definitions

def get_tags_mapping():
    modules_mapping = treeutils.SimpleRouterTree()
    for app in apps.get_app_configs():
        modules_mapping.index(app.module.__spec__.name, app.label)
    return modules_mapping
        
def get_tags_from_paths(paths):
    all_tags = []
    for path, path_info in paths.items():
        for method, method_info in path_info.items():
            tags = set(method_info.get("tags", []))
            all_tags += tags
    return set(all_tags)

def get_tags(paths):
    all_tags = get_tags_from_paths(paths)
    tags = []
    for app in apps.get_app_configs():
        tag_name = app.label
        if not tag_name in all_tags:
            continue
        tag = {}
        tag["name"] = tag_name
        tag["description"] = gettext(app.verbose_name)
        tags.append(tag)
    return tags

def get_view_summary(view_doc):
    return view_doc.splitlines()[0]

def get_view_methods(view_doc):
    result = re.findall("@methods:(.+)", view_doc)
    if not result:
        return ""
    return [x.strip() for x in result[0].strip().split(",")]

def get_view_description(view_doc):
    view_description_lines = []
    for line in view_doc.splitlines():
        if "-"*8 in line:
            break
        else:
            view_description_lines.append(line)
    return "\n".join(view_description_lines)

def get_view_parameters(view_doc):
    parameters = []
    parameter_infos = re.findall("@parameter: (.+?) {{{(.*?)}}}?", view_doc, re.MULTILINE|re.DOTALL|re.S)
    for parameter_info in parameter_infos:
        payload_parameter = {}
        parameter_name, parameter_config = parameter_info
        payload_parameter["name"] = parameter_name
        try:
            parameter_config = yaml.safe_load(parameter_config)
        except Exception as error:
            parameter_config = {}
        payload_parameter.update(parameter_config)
        # fix payload_parameter["schema"]["$ref"] missing prefix problem
        if "schema" in payload_parameter:
            if "$ref" in payload_parameter["schema"]:
                if not payload_parameter["schema"]["$ref"].startswith("#/definitions/"):
                    payload_parameter["schema"]["$ref"] = "#/definitions/" + payload_parameter["schema"]["$ref"]
        # append paramter to parameters
        parameters.append(payload_parameter)
    return parameters

def get_view_responses(view_doc, view_func):
    responses = {}
    response_infos = re.findall("@response: (\\d+?) (OK|ERROR) (.*?) {{{(.*?)}}}", view_doc, re.MULTILINE|re.DOTALL|re.S)
    if not response_infos:
        return responses
    for response_info in response_infos:
        status_code, result_success_flag, result_description, result_data = response_info
        status_code = int(status_code)
        if not status_code in responses:
            responses[status_code] = {
                "description": ""
            }
        result_success_flag = result_success_flag.strip()
        if result_success_flag.lower() == "error":
            result_success_flag = False
        else:
            result_success_flag = True
        result_description = result_description.strip()
        try:
            result_data = yaml.safe_load(result_data)
        except Exception as error:
            logger.error(f"yaml.safe_load result_data failed: result_data={result_data}, error={error}...")
            result_data = ""
        if result_success_flag:
            result_data = json.dumps(view_func._django_apiview_main_wrapper.packer.pack_result(result_data), indent=4, ensure_ascii=False)
        else:
            result_data = json.dumps(view_func._django_apiview_main_wrapper.packer.pack_error(result_data), indent=4, ensure_ascii=False)

        responses[status_code]["description"] += result_description + "\n"
        responses[status_code]["description"] += "```\n"
        responses[status_code]["description"] += result_data + "\n"
        responses[status_code]["description"] += "```\n"
    return responses

def get_paths():
    paths = {}
    tags_mapping = get_tags_mapping()
    global_urls = get_resolver().reverse_dict
    for view_item  in global_urls.lists():
        # 获取当前视图的的处理函数
        view_func = view_item[0]
        if isinstance(view_func, str):
            view_func = resolve(reverse(view_func)).func
        # 获取当前视图的函数文档
        view_doc = view_func.__doc__ or ""
        if not view_doc:
            continue
        # 从函数文档中提取swagger信息
        view_summary = get_view_summary(view_doc)
        view_description = get_view_description(view_doc)
        view_parameters = get_view_parameters(view_doc)
        view_methods = get_view_methods(view_doc)
        view_responses = get_view_responses(view_doc, view_func)
        # 查找到当前视图函数所在应用标签，作为本接口的tag_name
        tag_name, _ = tags_mapping.get_best_match(view_func.__module__)
        if not tag_name:
            tag_name = "__all__"
        # 遍历所有视图公开的paths
        view_paths = view_item[1]
        for view_path in view_paths:
            path = "/" + view_path[0][0][0]
            paths[path] = {}
            view_info = {
                "tags": [tag_name],
                "summary": view_summary,
                "description": view_description,
                "operationId": view_func.__module__ + "." + view_func.__name__,
                "produces": [
                    "application/json",
                ],
                "parameters": view_parameters,
                "responses": view_responses,
            }
            for view_method in view_methods:
                paths[path][view_method] = view_info
    return paths 

# #############################################################################
# SWAGGER UI VIEWS
# #############################################################################
def swagger_ui_view(request):
    return render(request, "swagger-ui/swagger_ui.html", {
    })

def swagger_ui_meta(request):
    info = {
        "version": get_setting_value("DJANGO_APIVIEW_SWAGGER_UI_VERSION"),
        "title": get_setting_value("DJANGO_APIVIEW_SWAGGER_UI_TITLE"),
        "description": get_setting_value("DJANGO_APIVIEW_SWAGGER_UI_DESCRIPTION"),
        "termsOfService": get_setting_value("DJANGO_APIVIEW_SWAGGER_UI_TERMS_OF_SERVICE"),
        "contact": {
            "email": get_setting_value("DJANGO_APIVIEW_SWAGGER_UI_CONTACT_EMAIL"),
        }
    }
    securityDefinitions = get_setting_value("DJANGO_APIVIEW_SWAGGER_UI_SECURITY_DEFINITIONS", {})
    definitions = get_definitions()
    paths = get_paths()
    tags = get_tags(paths)
    return render(request, "swagger-ui/swagger_ui_meta.json", {
        "info_json": json.dumps(info, ensure_ascii=False),
        "tags_json": json.dumps(tags, ensure_ascii=False),
        "securityDefinitions_json": json.dumps(securityDefinitions, ensure_ascii=False),
        "definitions_json": json.dumps(definitions, ensure_ascii=False),
        "paths_json": jsonutils.simple_json_dumps(paths, ensure_ascii=False),
        "api_host": get_setting_value("DJANGO_APIVIEW_SWAGGER_UI_API_HOST", get_server_host()),
        "api_basepath": get_setting_value("DJANGO_APIVIEW_SWAGGER_UI_API_BASEPATH", "/"),
    }, content_type="application/json")

def swagger_ui_initializer(request):
    return render(request, "swagger-ui/swagger_ui_initializer.js", {
    }, content_type="application/javascript")
