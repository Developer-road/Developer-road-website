from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

# Import People class
from .models import People


class AboutView(ListView):
    """
    View that shows the list of all the existent blogs
    """
    model = People
    template_name = 'about/index.html'