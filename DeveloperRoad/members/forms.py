from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views


class SignUpForm(UserCreationForm):

    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'class': 'form-control bg-white border-left-0 border-md'}))
    first_name = forms.CharField(max_length=70, widget=forms.TextInput(
        attrs={'placeholder': 'First name', 'class': 'form-control bg-white border-left-0 border-md'}))
    last_name = forms.CharField(max_length=70, widget=forms.TextInput(
        attrs={'placeholder': 'Last name', 'class': 'form-control bg-white border-left-0 border-md'}))

    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name",
                  "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # self.fields["username"].widget.attrs["class"] = 'form-control bg-white border-left-0 border-md'

        # First password
        self.fields["password1"].widget.attrs["class"] = 'form-control bg-white border-left-0 border-md'
        self.fields["password1"].widget.attrs["placeholder"] = 'Password'

        # Password confirmation
        self.fields["password2"].widget.attrs["class"] = 'form-control bg-white border-left-0 border-md'
        self.fields["password2"].widget.attrs["placeholder"] = 'Confirm'


class UserEditForm(UserChangeForm):

    first_name = forms.CharField(max_length=70, widget=forms.TextInput(
        attrs={'placeholder': 'First name', 'class': 'form-control bg-white border-left-0 border-md'}))
    last_name = forms.CharField(max_length=70, widget=forms.TextInput(
        attrs={'placeholder': 'Last name', 'class': 'form-control bg-white border-left-0 border-md'}))
    description = forms.CharField(max_length=400, widget=forms.Textarea(
        attrs={'placeholder': 'Last name', 'class': 'form-control bg-white border-left-0 border-md'}))


    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "description","profile_image")



class MyPasswordChangeForm(auth_views.PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True,
                                          "class": "form-control bg-white border-left-0 border-md", "placeholder": "Old Password"}),
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True,
                                          "class": "form-control bg-white border-left-0 border-md", "placeholder": "New Password"}),
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True,
                                          "class": "form-control bg-white border-left-0 border-md", "placeholder": "Confirmation"}),
    )

