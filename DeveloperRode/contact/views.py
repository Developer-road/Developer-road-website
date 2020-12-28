from django.shortcuts import render
from django.views import View

class ContactView(View):
    """
    Contact page of the site
    """
    def get(self, request):
        
        return render(request, 'contact/index.html')