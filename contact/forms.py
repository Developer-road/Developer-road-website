from django import forms


class ContactEmailForm(forms.Form):
    name = forms.CharField(max_length=120, widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Your name here"}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Your email"}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control", "placeholder": "Your message here"}))
