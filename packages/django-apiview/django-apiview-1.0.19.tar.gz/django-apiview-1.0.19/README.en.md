# django-apiview

A set of django tools to help you create JSON service.

## Install

```
pip install django-apiview
```

## Installed Decorators

- @apiview
- @requires(*required_parameter_names)
- @choices(field, choices, allow_none=False)
- @between(field, min, max, include_min=True, include_max=True, annotation=Number, allow_none=False)
- @rsa_decrypt(field, private_key_instance)
- @meta_variable(variable_name, meta_name)
- @cache(key, expire=None, cache_name="default", get_from_cache=True, set_to_cache=True)
- @safe_apiview(get_client_rsa_publickey, **kwargs)
- @decode_encrypted_data(result_encoder=cipherutils.SafeBase64Encoder(), privatekey=None, server_rsa_privatekey_filedname="RSA_PRIVATEKEY", encrypted_password_fieldname="encryptedPassword", encrypted_data_fieldname="encryptedData")
- @check_aclkey(aclkey=None, aclkey_field_name="aclkey")
    - default aclkey=settings.DJANGO_APIVIEW_ACLKEY
- @string_length_limit

**Note:**

- @apiview
    1. apiview = Apiview(SimpleJsonPacker())
- @safe_apiview(...)
    1. Requires django_middleware_global_request, see django_middleware_global_request's usage at https://pypi.org/project/django-middleware-global-request/.
    1. Requires server rsa settings: RSA_PRIVATEKEY_STRING, RSA_PRIVATEKEY (load RSA_PRIVATEKEY_STRING as RsaKey)
    1. Callback function get_client_rsa_publickey defines: `def get_client_rsa_publickey(client_id): pass`
    1. kwargs:
        1. client_id_fieldname = "clientId"
        1. client_rsa_publickey_fieldname = "CLIENT_RSA_PUBLICKEY"
        1. result_encoder = cipherutils.SafeBase64Encoder()
        1. server_rsa_privatekey_filedname = RSA_PRIVATEKEY
        1. encrypted_password_fieldname = encryptedPassword
        1. encrypted_data_fieldname = encryptedData
        1. packer_class = SafeJsonResultPacker
        1. password_length = 32
- @cache(...)
    1. Optional setting: DJANGO_APIVIEW_DISABLE_CACHE_HEADER_NAME = "HTTP_DISABLE_CACHE"
    1. Optional setting: DJANGO_APIVIEW_DEFAULT_CACHE_EXPIRE = None 

## Usage


**Note:**

- Apiview always set csrf_exempt=True.
- @apiview or @safe_apiview decorator must be the first decorator.
- Return raw data without serialized, we'll do result pack for you.


**app/views.py**

```python
import time
from django_apiview.views import apiview
from django_apiview.views import requires
from django_apiview.views import choices
from django_apiview.views import between

@apiview
def ping():
    return "pong"

@apiview
def timestamp():
    return int(time.time())

@apiview
@requires("msg")
def echo(msg: str):
    return msg

@apiview
def getBooleanResult(value : bool):
    return value

@apiview
def getIntegerResult(value: int):
    return value

@apiview
def getBytesResult(value: bytes):
    return value

@apiview
@choices("op", ["+", "-", "*", "/"])
@between("a", 2, 10, include_min=False)
@between("b", 2, 10, include_max=False)
def calc(a: int, op: str, b: int):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b

@safe_apiview(get_client_rsa_publickey=get_client_rsa_publickey)
def safe_ping():
    return "pong"

```

## About swagger-ui

django-apiview has it's own swagger-ui starts from version v1.0.x. All swagger-ui settings are not influence the view process.

### Enable swagger-ui for the site

1. Enable swaggeer in `pro/settings.py`, and add swagger-ui admin users.

    ```
    DJANGO_APIVIEW_ENABLE_SWAGGER = True
    ```

1. Add swagger views in `pro/urls.py`.

    ```
    urlpatterns = [
        path("apiview/", include("django_apiview.urls")),
    ]
    ```

1. After you setup your swagger-ui views, open your brwoser and visit: http://127.0.0.1:8000/apiview/swagger-ui.html. Login required. You must be a superadmin or the user who has django_apiview_swagger_user permission.

### Enable swagger-ui for a view function

1. Only views with @apiview decorator will be shown in swagger-ui.
1. Write swagger-ui meta in the view's doc string.
1. `@methods:` is required to take a view into swagger-ui.

### Swagger-ui doc string rules

1. The first line of doc string in the view's summary.
1. The lines of doc string before -------- are the view's description.
1. You should put swagger-ui meta lines after --------, so that they will not mass up the view's description.
1.` @methods:` Required. It provides allowed request methods for the view. 
    `@methods: get`, means the view accepts GET method, and there will be one GET path in swagger-ui.
    `@methods: post`, means the view accepts POST method, and there will be on POST path in swagger-ui.
    `@methods: get, post`, means the view accepts both GET and POST methods, and there will be two path in swagger-ui.
    If NO `@methods:` setting was given, the api will NOT be shown in swagger-ui.
1. `@parameter:` Optional, multiple.
    ```
    @parameter: body {{{
        in: body
        required: true
        description: 表单数据
        schema:
          $ref: path.to.Model
    }}}
    ```
    This means the request body is in json format, and matches with `path.to.Model` scheme.

    ```
    @parameter: body {{{
        in: body
        required: true
        description: 表单数据
        example:
          field1: value1
          field2: value2
          field3:
            - 1
            - 2
            - 3
          field4: value4
    }}}
    ```
1. `@response`: Optional, multiple.
    ```
    @response: 200 OK Correct response {{{
        field1: value1
        field2: value2
    }}}
    ```
    This means "Correct response" with http status code 200 and field1 and field2 data values.

### Example views with swagger-ui enabled

```
from django_apiview.views import apiview

@apiview
def ping():
    """Always returns "pong" string。

    --------
    @methods: get
    @response: 200 OK "Correct response" {{{
        "pong"
    }}}
    @response: 200 ERROR "Something goes wrong" {{{
        {
            "code": 1234,
            "message": "Error reason."
        }
    }}}
    """
    return "pong"


@apiview
@string_length_limit("msg", max_length=4096, min_length=2)
def echo(msg: str):
    """Always returns msg input.

    --------
    @methods: post
    @parameter: body {{{
        in: body
        required: true
        example:
          msg: "hello world"
    }}}
    @response: 200 OK "Correct response" {{{
        "hello world"
    }}}
    @response: 500 ERROR "Something goes wrong" {{{
        {
            "code": 1234,
            "message": "Error reason."
        }
    }}}
    """
    return msg
```

## Releases

### v0.1.0

- First release.

### v0.1.1 

- Add PAYLOAD injection, PAYLOAD field has low priority. 

### v0.1.2

- Fix form process problem.

### v0.1.3

- Add logging while getting result failed in @apiview.
- Add Map, List annotations.

### v0.2.0

- Using fastutils.typingutils for annotation cast.
- Add result pack mechanism.
- Move example views from the main app to example app and the example app is not include in published package.

### v0.3.1 (`WARN`: NOT backward compatible.)

- Change app name from `apiview` to `django_apiview`.
- Add parameter validators.

### v0.3.2

- Add Apiview class based implementation.
- Add setup_result_packer api.<
- Rename simple_json_result_packer to simple_result_packer.

### v0.3.3

- Add rsa_decrypt decorator.

### v0.3.4

- Fix BizError class check problem.

### v0.4.0

- Add meta_variable decorator.
- Datetime value encode to native time, and in format like `2020-08-06 14:41:00`.

### v0.5.0

- Add cache decorator.
- Add func's default values to View.data.

### v0.6.0

- Add safe_apiview.

### 0.7.0

- Add batch_mode parameter support for cache. 

### v0.8.0

- Add ApiviewDecorator to make decorator programming easier.
- Fix some function reference problem. 

### v0.8.3

- Fix variable reference problem.

### v0.8.4

- Add cache entry_point manage.

### v0.8.6

- Add check_aclkey.
- Parse json data before doing data unpack.

### v0.8.8

- Use logger.exception instead of logger.error, so that we get running stack message.
- Use `cache.expire(key, expire)` after `cache.set(key, value)` instread of `cache.set(key, value, keepttl=expire)`.

### v0.8.9

- Fix boolean calc problem.

### v0.9.2 (`WARN`: function removed for performence problem, use nginx access log instread)

- Add log_api_response_time.

### v0.9.7

- Add string_length_limit.
- Fix SimpleJsonResultPacker.unpack.

### v0.9.20

- @requires support A-OR-B model parameters check.
- Fix SimpleJsonResultPacker.unpack if missing success filed.
- Remove api response time log models. Waste resources. Get response time from nginx access log instread.
- make cache cleaners setup easy. 

### v0.9.21

- Update dependent packages' version. 

### v0.9.23

- Handle json dumps error at the last step.
- Create response instance first so that you can handle the response instance: _django_apiview_response.
- rsa_decrypt fix for None problem.

### v0.9.25

- Fix empty result problem.
- Fix logging problem.

### v0.9.26

- Add cookie_variable. 

### v0.9.27

- Fix `between` not using `annotation` parameter problem.

### v0.9.28

- SimpleCacheCleaner Cache cleaner should only do once per request. 

### v0.9.29

- Fix pack_result parameter conflict problem.
