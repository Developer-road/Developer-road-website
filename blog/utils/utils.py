"""
Utilities
"""


# Django
from django.db.models import Count

# Models
from blog.models import Category, Post

# Get the categories objects with the mosts posts
ALL_CATEGORIES = Category.objects.annotate(
    most_posts=Count("linked_posts")).order_by("-most_posts")

# Small gif for Set Up model testing
SMALL_GIF = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
    b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
    b'\x02\x4c\x01\x00\x3b'
)

# Simple image for testing porpuses
SIMPLE_IMAGE = b"Lets grab a \xf0\x9f\x8d\x95!"

LIKED_POSTS = Post.objects.annotate(liked=Count("upvotes")).order_by("liked")