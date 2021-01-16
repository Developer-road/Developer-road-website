from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
# Create your views here.
from .forms import SignUpForm, UserEditForm, MyPasswordChangeForm


class SignUpView(generic.CreateView):
    """
    Allow the User to Create a New Account
    """
    form_class = SignUpForm 
    template_name = "registration/singup.html"
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    """
    Allows the User to Edit their Profile
    """
    form_class = UserEditForm 
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy('blog:blog_page')

    def get_object(self):
        return self.request.user


class ChangePasswordView(auth_views.PasswordChangeView):
    form_class = MyPasswordChangeForm 
    template_name = "registration/change_password.html"
    success_url = reverse_lazy('members:change_password_success')

class ChangePasswordSuccessView(TemplateView):
    template_name = "registration/change_password_success.html"


