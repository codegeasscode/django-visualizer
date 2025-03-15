from django.urls import include, path

urlpatterns = [
    path("", include("visualizer_app.urls")),
]
