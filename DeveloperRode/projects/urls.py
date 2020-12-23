from django.urls import path
from .views import ProjectsHome, ProjectsDetail

app_name = 'my_projects'
urlpatterns = [
    path("", ProjectsHome.as_view(), name="projects"),
    path("<int:project_id>/", ProjectsDetail.as_view(), name="detail-project"),
]
