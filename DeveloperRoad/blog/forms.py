from django import forms
from django_bleach.forms import BleachField

from .models import Post, Category, Comment


class PostForm(forms.ModelForm):
    class Meta:
        """
        Returns the form of  the add post page
        """
        model = Post
        fields = ('title', 'description', 'header_image', 'body', 'category',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', "placeholder": "An awesome title 🤓"}),
            # 'author': forms.TextInput(attrs={'class': 'form-control', "value":"", "id": "jhsdfjkhasdfjljadklasfdkjdfjkasdfkn", "type": "hidden"}),
            'description': forms.Textarea(attrs={'class': 'form-control', "placeholder": "Describe your Post briefly"}),
            # 'body': forms.Textarea(attrs={'class': 'form-control',"placeholder": "Unleash your creativity in the Post"}),
            'body': BleachField(),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        """
        Returns the form of  the add post page
        """
        model = Post
        fields = ('title', 'description', 'header_image', 'body', 'category',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'body': BleachField(),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        """
        Returns the form of the add category page
        """
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        """
        Returns the form of the comment  page
        """
        model = Comment
        fields = ('body',)
        widgets = {
            'body': BleachField()
        }
