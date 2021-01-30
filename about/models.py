from django.db import models

# Create your models here.

from django.urls import reverse


# class People(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True)
#     person_picture = models.ImageField(upload_to="images/about/")

#     def __str__(self):
#         """
#         Show the name of the person in the admin Page
#         """
#         return str(self.name)

#     def get_absolute_url(self):
#         return reverse("about:about_page")
    