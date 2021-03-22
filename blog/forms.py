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
            'description': forms.Textarea(attrs={'class': 'form-control', "placeholder": "Describe your Post briefly"}),
            'body': BleachField(),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'header_image': forms.FileInput(attrs={'class': 'form-control'}),
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
            'header_image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        """
        Returns the form of the add category page
        """

        model = Category
        fields = ('name', 'image', 'description')
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):

        data = self.cleaned_data.get('name').lower()

        if Category.objects.filter(name__iexact=data).count() >= 1:
            raise forms.ValidationError('Sorry that category already exist')

        return data



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

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields["body"].required = True

