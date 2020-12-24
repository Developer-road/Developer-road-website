from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=30)
    image = models.ImageField(blank=True, null=True)
    project_url = models.URLField(null=True)

    def __str__(self):
        return self.title
    