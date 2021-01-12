from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        """
        Returns the form of  the add post page
        """
        model = Post
        fields = ('title', 'author', 'description', 'body', 'category',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', "placeholder": "An awesome title 🤓"}),
            'author': forms.TextInput(attrs={'class': 'form-control', "value":"", "id": "jhsdfjkhasdfjljadklasfdkjdfjkasdfkn", "type": "hidden"}),
            'description': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Describe your Post briefly"}),
            'body': forms.Textarea(attrs={'class': 'form-control',"placeholder": "Unleash your creativity in the Post"}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        """
        Returns the form of  the add post page
        """
        model = Post
        fields = ('title', 'description', 'body', 'category',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
