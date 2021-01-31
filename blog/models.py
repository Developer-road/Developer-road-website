from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# For pub date
from datetime import date, datetime

# Import Custom user
from django.conf import settings

from django_bleach.models import BleachField


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(default="This category hasn't a description yet", blank=True, null=True)

    def __str__(self):
        """
        Show the category name in the admin Page
        """
        return self.name

    def get_absolute_url(self):
        return reverse("blog:blog_page")


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    header_image = models.ImageField(
        blank=True, null=True, upload_to="images/post_header/")
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    # body = models.TextField()
    body = RichTextField()
    upvotes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="post_votes")

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

    @property
    def number_of_comments(self):
        return Comment.objects.filter(post=self).count()

class Comment(models.Model):
    """
    The comment system in The Blog
    """
    post = models.ForeignKey(
        Post, verbose_name="comment", on_delete=models.CASCADE)
    # commenter = models.CharField(max_length=255, default="Anonymous")
    commenter = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = RichTextField(config_name="comment")
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.post.title)}, {str(self.commenter)}"
