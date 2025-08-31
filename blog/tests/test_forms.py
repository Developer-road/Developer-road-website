"""
Blog Forms testing
"""

# Django test case
from django.test import TestCase


# Forms
from blog.forms import (
    # POSTS
    PostForm,
    EditPostForm,

    # CATEGORIES
    CreateCategoryForm,
    EditCategoryForm,

    # Create comment form
    CommentForm,
)

# Models

from blog.models import Category

# Simple image
from blog.utils import SIMPLE_UPLOADED_GIF


class SetUpMixin:

    def setUp(self):
        # CONSTANTS

        self.title = "A cool blog title"

        self.description = "This is a test post"

        self.body = "Hi there this is the body of the post"

        self.category_name = "A category"

        self.category_desc = "A category is a word :)"

        self.category = Category.objects.create(name="category1")

        self.comment_body = "Hi there this is a cool comment :)))"


class TestForms(SetUpMixin, TestCase):

    ################
    #    POSTS     #
    ################

    def test_create_post_form_full_data(self):

        data = {
            "title": self.title,
            "description": self.description,
            "header_image": SIMPLE_UPLOADED_GIF,
            "body": self.body,
            "category": self.category,
        }

        form = PostForm(data=data)

        self.assertTrue(form.is_valid())

    def test_create_post_form_required_fields(self):

        data = {
            "title": self.title,
            "body": self.body,
        }

        form = PostForm(data=data)

        self.assertTrue(form.is_valid())

    def test_create_post_form_no_data(self):

        data = {}

        form = PostForm(data=data)

        self.assertFalse(form.is_valid())

        self.assertEqual(len(form.errors), 2)

    def test_edit_post_form_all_data(self):

        data = {
            "title": self.title,
            "description": self.description,
            "header_image": SIMPLE_UPLOADED_GIF,
            "body": self.body,
            "category": self.category,
        }

        form = PostForm(data=data)

        self.assertTrue(form.is_valid())

    def test_edit_post_form_partial_data(self):

        data = {"title": self.title}

        form = PostForm(data=data)

        self.assertFalse(form.is_valid())

        self.assertEqual(len(form.errors), 1)

    ################
    #  CATEGORIES  #
    ################

    def test_create_category_form_all_data(self):

        data = {
            "name": self.category_name,
            "image": SIMPLE_UPLOADED_GIF,
            "description": self.category_desc,
        }

        form = CreateCategoryForm(data=data)

        self.assertTrue(form.is_valid())

    def test_create_category_form_required_data(self):
        data = {"name": self.category_name}

        form = CreateCategoryForm(data=data)

        self.assertTrue(form.is_valid())

    def test_create_category_form_no_data(self):

        data = {}

        form = CreateCategoryForm(data=data)

        self.assertFalse(form.is_valid())

        self.assertEqual(len(form.errors), 1)

    def test_create_category_form_category_already_created(self):

        data = {
            "name": self.category.name.upper(),
        }

        form = CreateCategoryForm(data=data)

        self.assertFalse(form.is_valid())

        self.assertEqual(len(form.errors), 1)


    def test_edit_category_form_category_already_created(self):

        data = {
            "name": "category1"
        }

        form_ = EditCategoryForm(data=data)

        # For some reason the form isn't valid :()
        self.assertFalse(form_.is_valid())

    def test_create_comment_form_all_data(self):

        data = {
            "body": self.comment_body
        }

        form = CommentForm(data=data)

        self.assertTrue(form.is_valid())

    def test_create_comment_form_no_data(self):

        data = {}

        form = CommentForm(data=data)

        self.assertFalse(form.is_valid())

        self.assertEqual(len(form.errors), 1)
