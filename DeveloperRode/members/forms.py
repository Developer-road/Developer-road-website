from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):

    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'placeholder':'Email', 'class': 'form-control bg-white border-left-0 border-md'}))
    first_name = forms.CharField(max_length=70, widget=forms.TextInput(
        attrs={'placeholder':'First name','class': 'form-control bg-white border-left-0 border-md'}))
    last_name = forms.CharField(max_length=70, widget=forms.TextInput(
        attrs={'placeholder':'Last name','class': 'form-control bg-white border-left-0 border-md'}))

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
