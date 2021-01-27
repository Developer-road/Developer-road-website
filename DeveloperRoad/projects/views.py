from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from django.urls import reverse_lazy

from .models import Project
from .forms import AddProjectForm


# Create your views here.
class ProjectsHome(ListView):
    """
    Returns the projects page
    """
    model = Project
    template_name = 'projects/index.html'
    ordering = ["-id"]

    paginate_by = 6


class ProjectsDetail(DetailView):
    """
    Returns the projects page
    """
    model = Project
    template_name = 'projects/details.html'


class ProjectCreateView(CreateView):
    model = Project
    template_name = "projects/create.html"
    form_class = AddProjectForm

    success_url = reverse_lazy("projects:my_projects")


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = "projects/edit.html"
    form_class = AddProjectForm
    success_url = reverse_lazy("projects:my_projects")
