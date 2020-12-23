from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Project

# Create your views here.
class ProjectsHome(View):
    def get(self, request):
        """
        Returns the projects page
        """
        my_projects = Project.objects.all()
        
        context = {"projects": my_projects}
        
        return render(request, 'projects/index.html', context)


class ProjectsDetail(View):
    def get(self, request, project_id):
        """
        Returns the projects page
        """
        detail_project = get_object_or_404(Project, pk=project_id)
        context = {"project": detail_project}
        return render(request, 'projects/details.html',context)