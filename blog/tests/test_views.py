from django.test import TestCase

from django.urls import reverse

from django.contrib.auth import get_user_model as User

from blog.models import (
    Post,
    Comment,
    Category
)


class SetUpViewsMixin:

    def setUp(self):

        self.user1 = User().objects.create(
            email="user@user.com",
            first_name="user",
            last_name="1",
            password="Userpassword"
        )

        self.user2 = User().objects.create(
            email="user2@user.com",
            first_name="user",
            last_name="2",
            password="Userpassword"
        )

        self.category1 = Category.objects.create(
            name="cool-category"
        )

        self.post1 = Post.objects.create(
            title="A cool title",
            author=self.user1,
            body="he he he ",
            category=self.category1
        )

        self.post2 = Post.objects.create(
            title="A cool title",
            author=self.user2,
            body="he he he ",
            category=self.category1
        )

        # Url patterns

        self.list_blog_url = reverse("blog:blog_page")

        self.list_blog_most_liked_url = reverse("blog:blog_liked_page")

        self.list_categories_url = reverse("blog:categories_page")

        self.search_url = reverse("blog:search")

        # CRUD

        self.create_post_url = reverse("blog:add_post")

        self.create_category_url = reverse("blog:add_category")

        # Details

        #  CRUD

        self.detail_edit_post_url = reverse(
            "blog:edit_page", args=[self.post1.id])

        self.detail_delete_post_url = reverse(
            "blog:delete_page", args=[self.post2.id])

        # Detail view

        self.detail_post_url = reverse(
            "blog:article_page", args=[self.post1.id])


        self.detail_category_url = reverse("blog:category_page", args=[
                                           self.category1.name.replace(" ", "-")])
        
        self.detail_edit_category_url = reverse("blog:category_edit", args=[self.category1.id])

class TestViews(SetUpViewsMixin,TestCase):

    def test_blog_view_GET(self):

        # response = self.client.get(self.list_blog_url)

        pass
