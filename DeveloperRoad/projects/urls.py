from django.urls import path
from .views import ProjectsHome, ProjectsDetail

app_name = 'projects'
urlpatterns = [
    path("", ProjectsHome.as_view(), name="my_projects"),
    path("<int:pk>/", ProjectsDetail.as_view(), name="detail-project"),
]
