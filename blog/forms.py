from django import forms
from django_bleach.forms import BleachField

from .models import Post, Category, Comment


class BaseCRUDPostForm(forms.ModelForm):
    class Meta:
        """
        Returns the form of  the add post page
        """
        model = Post

        fields = ('title', 'description', 'header_image', 'body', 'category',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            "placeholder": "An awesome title 🤓"}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 "placeholder": "Describe your Post briefly"}),
            'body': BleachField(),

            'category': forms.Select(attrs={'class': 'form-control'}),

            'header_image': forms.FileInput(attrs={'class': 'form-control'}), }


class PostForm(BaseCRUDPostForm):
    """
    Form used to create a Post
    """

class EditPostForm(BaseCRUDPostForm):
    """
    Form used to edit a Post
    """


class BaseCRUDCategoryForm(forms.ModelForm):
    """
    Base CRUD operations for categories model
    """
    class Meta:
        """
        Returns the form of the add category page
        """

        model = Category
        fields = ('name', 'image', 'description')
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class EditCategoryForm(BaseCRUDCategoryForm):
    """
    Edit category form for Category edit page
    Only available for admins
    """


class CreateCategoryForm(BaseCRUDCategoryForm):

    def clean_name(self):

        data = self.cleaned_data.get('name')

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
