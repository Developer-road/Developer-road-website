from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
class Home(View):
    def get(self, request):
        """
        View that returns the home view
        """
        return render(request, 'home/index.html')

def handler404(request):
    """
    Handles the 404 Page to all the Website
    """
    return render(request, "home/handler.html")
