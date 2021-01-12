from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=30)
    image = models.ImageField(null=True, upload_to="images/projects")
    project_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    