from django.urls import path
from .views import visualise

urlpatterns = [
    path("visualise/", visualise, name="visualise"),
]
