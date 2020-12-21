from django.urls import path
from .views import Projects

app_name = 'projects'
urlpatterns = [
    path("", Projects.as_view())
]
