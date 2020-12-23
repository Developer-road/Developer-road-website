from django.shortcuts import render
from django.views import View

# Create your views here.
class AboutView(View):
    
    def get(self, request):
        """
        Returns the about page
        """
        return render(request,'about/index.html')