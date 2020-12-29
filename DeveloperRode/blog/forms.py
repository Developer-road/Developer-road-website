from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        """
        Returns the form of  the add post page
        """
        model = Post
        fields = ('title', 'author', 'meta_description', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'meta_description': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        """
        Returns the form of  the add post page
        """
        model = Post
        fields = ('title', 'meta_description', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'meta_description': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
