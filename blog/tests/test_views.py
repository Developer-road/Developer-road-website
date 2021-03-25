from django.test import TestCase

from django.urls import reverse

from blog.models import (
    Post,
    Comment,
    Category
)

class SetUpMixin:

    def setUp(self):
        pass
