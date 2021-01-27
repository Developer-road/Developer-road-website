from django.urls import path
from .views import ProjectsHome, ProjectsDetail,ProjectCreateView, ProjectUpdateView

app_name = 'projects'
urlpatterns = [
    path("", ProjectsHome.as_view(), name="my_projects"),
    path("<int:pk>/", ProjectsDetail.as_view(), name="detail-project"),
    path("add_project/", ProjectCreateView.as_view(), name="add"),
    path("<int:pk>/edit/", ProjectUpdateView.as_view(), name="edit"),
]
