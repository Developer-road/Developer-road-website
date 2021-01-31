from django.db import models

# Create your models here.

def get_image_extension(filename):
    if "." in filename:
        return filename.split(".")[-1]
    else:
        return None


def get_project_image(self, filename):
    """
    Returns the profile name path to store
    """
    extension = get_image_extension(filename)

    if extension is not None:
        return f"images/projects/{self.title}/profile_image.{extension}"
    else:
        return f"images/projects/{self.title}/profile_image.png"

class Project(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    technology = models.CharField(max_length=30)
    image = models.ImageField(null=True, upload_to=get_project_image, blank=True)
    skill = models.CharField(max_length=200, null=True, blank=True)
    project_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

