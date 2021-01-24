from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

# Create your views here.
from .forms import SignUpForm, UserEditForm, MyPasswordChangeForm

from blog.models import Post

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
    model = get_user_model()
    form_class = UserEditForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy('members:edit_success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile_user"] = get_object_or_404(self.model, id=self.kwargs['pk'])
        return context


class ChangePasswordView(auth_views.PasswordChangeView):
    form_class = MyPasswordChangeForm
    template_name = "registration/change_password.html"
    success_url = reverse_lazy('members:change_password_success')


class ChangePasswordSuccessView(TemplateView):
    template_name = "registration/change_password_success.html"


class EditProfileSuccessView(TemplateView):
    template_name = "registration/edit_profile_success.html"


class ShowProfileView(DetailView):
    model = get_user_model()
    template_name = "registration/user_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        requested_user = get_object_or_404(self.model, id=self.kwargs['pk'])
        context["requested_user"] = requested_user
        # Blog Stuff Only use in Blog Project
        try:
            context["user_posts"] = list(Post.objects.filter(author_id=requested_user.id))
        except Post.DoesNotExist:
            context["user_posts"] = None
        
        context["image_hidden"] = True
        
        return context
