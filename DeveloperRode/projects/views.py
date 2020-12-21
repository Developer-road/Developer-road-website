from django.shortcuts import render
from django.views import View


# Create your views here.
class Projects(View):
    def get(self, request):
        """
        Returns the projects page
        """
        return render(request, 'projects/index.html')