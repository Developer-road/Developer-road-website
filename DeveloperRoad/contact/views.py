from django.shortcuts import render
from django.views.generic import TemplateView

class ContactView(TemplateView):
    """
    Contact page of the site
    """
    template_name = "contact/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[""] = ""
        return context
    