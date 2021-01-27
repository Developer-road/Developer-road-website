from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Import People class

class AboutView(TemplateView):
    """
    View that shows the list of all the existent blogs
    """
    template_name = 'about/index.html'