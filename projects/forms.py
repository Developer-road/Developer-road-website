from django import forms
from .models import Project


class AddProjectForm(forms.ModelForm):
    """
    Show the add project form if the user is admin
    """
    class Meta:
        model = Project        
        fields = ("title", "description", "skill","technology", "image", "project_url")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', "placeholder": "An awesome project title 🤓"}),
            'description': forms.Textarea(attrs={'class': 'form-control', "placeholder": "Describe your Project briefly"}),
            'technology': forms.TextInput(attrs={'class': 'form-control'}),
            'project_url': forms.TextInput(attrs={'class': 'form-control'}),
            'skill': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "The skill that you've learned with the Project"}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }