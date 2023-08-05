
window.onload = function() {
  var server = window.location.protocol + "//" + window.location.host;
  window.ui = SwaggerUIBundle({
    urls: [{
      url: server + "{% url "django_apiview_swagger_ui_meta" %}",
      name: "default"
    }],
    dom_id: '#swagger-ui',
    deepLinking: true,
    presets: [
      SwaggerUIBundle.presets.apis,
      SwaggerUIStandalonePreset
    ],
    plugins: [
      SwaggerUIBundle.plugins.DownloadUrl
    ],
    layout: "StandaloneLayout"
  });

};
