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
    """
    Categories system, organizes the blog topics.

    params: name, date (auto), description, image
    """

    # The name for the category
    name = models.CharField(max_length=100,
                            unique=True)

    date = models.DateTimeField(auto_now_add=True,
                                blank=True,
                                null=True)

    # A short description for the category
    description = models.TextField(
        default="This category hasn't a description yet",
        blank=True,
        null=True)

    # Category image
    image = models.ImageField(
        upload_to="images/categories/",
        blank=True,
        null=True)


    def __str__(self):
        """
        Show the category name in the admin Page
        """
        return self.name

    def get_absolute_url(self):
        return reverse("blog:category", args=[self.name.lower().replace(" ", "-")])

    @property
    def number_of_category_posts(self):
        category_posts = Post.objects.filter(category_id=self.id).count()
        return category_posts


class Post(models.Model):

    title = models.CharField(max_length=200)

    # Foreign key with the custom user model
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Optional image uploaded to media files
    header_image = models.ImageField(
        blank=True,
        null=True,
        upload_to="images/post_header/")

    # Date and hour of the creation
    date = models.DateTimeField(auto_now_add=True,
                            blank=True,
                            null=True)

    # An optional description text
    description = models.TextField(blank=True,
                                   null=True)

    # A optional relation with the category
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="linked_posts")

    # The content of the post
    body = RichTextField()

    # A relation, between the custom user model and the post
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
        
        return reverse("blog:article", kwargs={"pk": self.pk})

    @property
    def number_of_comments(self):
        return Comment.objects.filter(post=self).count()


class Comment(models.Model):
    """
    The comment system in The Blog
    """

    # Assigned Post
    post = models.ForeignKey(
        Post, verbose_name="comment", on_delete=models.CASCADE)

    # The user that made the comment
    commenter = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # The comment itself. It has bold, italic, link and code.
    body = RichTextField(config_name="comment")

    # The date and hour the comment was added
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{str(self.post.title)}, {str(self.commenter)}"
