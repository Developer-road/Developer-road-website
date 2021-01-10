from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# For pub date
from datetime import date, datetime


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Show the category name in the admin Page
        """
        return self.name

    def get_absolute_url(self):
        return reverse("blog:blog_page")

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True) 
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = models.TextField()
    upvotes = models.ManyToManyField(User, related_name="post_votes")
    
    def total_likes(self):
        """
        Returns total likes in the page
        """
        return self.upvotes.count()

    def __str__(self):
        """
        Show the title and the author in the admin Page
        """
        return self.title + " by " + str(self.author)

    def get_absolute_url(self):
        return reverse("blog:article_page", kwargs={"pk": self.pk})
    