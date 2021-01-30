from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.core.mail import send_mail

# Contact form
from .forms import ContactEmailForm


class ContactView(FormView):
    """
    Contact page of the site
    """
    template_name = "contact/index.html"
    form_class = ContactEmailForm
    success_url = reverse_lazy("contact:success")


    def form_valid(self, form):
        message = "{name} / {email} said: ".format(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'))
        message += "\n\n{0}".format(form.cleaned_data.get('message'))

        send_mail(
            subject=form.cleaned_data.get('name').strip(),
            message=message,
            from_email='danidiazgon@protonmail.com',
            recipient_list=["danieldiazgonza52@gmail.com"],
        )
        return super(ContactView, self).form_valid(form)       


class ContactSuccessView(TemplateView):
    template_name = "contact/success.html"