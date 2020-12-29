from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# For pub date
from datetime import date, datetime

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True) 
    meta_description = models.TextField(blank=True, null=True)
    body = models.TextField()
    
    def __str__(self):
        """
        Show the title and the author in the admin Page
        """
        return self.title + " by " + str(self.author)

    def get_absolute_url(self):
        return reverse("blog:article_page", kwargs={"pk": self.pk})
    