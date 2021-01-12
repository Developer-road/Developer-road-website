from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Project

# Create your views here.
class ProjectsHome(ListView):
    """
    Returns the projects page
    """
    model = Project
    template_name = 'projects/index.html'
    ordering = ["-id"]

class ProjectsDetail(DetailView):
    """
    Returns the projects page
    """
    model = Project
    template_name = 'projects/details.html'