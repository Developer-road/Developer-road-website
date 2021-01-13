from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.
from .forms import SignUpForm

class SignUpView(generic.CreateView):
    form_class = SignUpForm 
    template_name = "registration/singup.html"
    success_url = reverse_lazy('login')
