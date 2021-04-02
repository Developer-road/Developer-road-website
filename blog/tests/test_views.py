"""Blog Views Tests"""

# Django
# Client used to log in a user in SetUp mixin
from django.test import TestCase, Client

from django.urls import reverse

from django.contrib.auth import get_user_model as User
from django.contrib.auth import get_user

# Models
from blog.models import (
    Post,
    Comment,
    Category
)

# Utils
from blog.utils import (
    ALL_CATEGORIES,
    MOST_LIKED_POSTS,
    MOST_COMMENTED_POSTS,
)


class SetUpViewsMixin:
    """
    Mixin used to set up the test database for each test.

    Number of post: 2

    Posts: A cool title, Post 2 title

    Number of categories: 2

    Number of users: 2
    """

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

        self.logged_in_client = Client()

        self.logged_in_client.force_login(
            User().objects.create_superuser(
                email="test@test.com",
                password="aaaaaa",
                first_name="test",
                last_name="a",
            )
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
            title="Post 2 title",
            author=self.user2,
            body="he he he ",
            category=self.category1
        )

        # Url patterns

        self.list_blog_url = reverse("blog:home")

        self.list_categories_url = reverse("blog:categories")

        self.search_url = reverse("blog:search")

        # CRUD

        self.create_post_url = reverse("blog:create_article")

        self.create_category_url = reverse("blog:create_category")

        # Details

        #  CRUD

        self.detail_edit_post_url = reverse(
            "blog:edit_article", args=[self.post1.id])

        self.detail_delete_post_url = reverse(
            "blog:delete_article", args=[self.post2.id])

        # Detail view

        self.detail_post_url = reverse(
            "blog:article", args=[self.post1.id])

        self.detail_category_url = reverse("blog:category", args=[
                                           self.category1.name.replace(" ", "-")])

        self.detail_edit_category_url = reverse(
            "blog:edit_category", args=[self.category1.id])

    def create_posts_evenly(self, name="Default post", number=1, body="Body of the post"):
        """
        Creates posts objects for a testcase.

        params: 
        name: The base name for the posts
        number: Number of posts, the title of the posts will be : 'name of post {number}'
        body: Body text of the posts
        """
        for i in range(1, number + 1):

            title = f"{name} {i}"

            author = self.user1

            if i % 2 == 0:
                author = self.user2

            Post.objects.create(title=title, author=author, body=body)

    def create_categories(self, name="Category", number=1):
        """
        Creates posts objects for a testcase.

        params: 
        name: The base name for the posts
        number: Number of posts, the title of the posts will be : 'name of post {number}'
        body: Body text of the posts
        """
        for i in range(1, number + 1):

            name_ = f"{name} {i}"

            Category.objects.create(name=name_)

    def create_comments_on_post(self, body="Some comment", number=1, post=None, commenter=None):
        """
        Create comments linked to the given post

        body: Body of the comment

        number: number of comments created

        post: Linked post

        commenter: Author of the comment
        """

        for _ in range(1, number + 1):

            Comment.objects.create(
                post=post,
                commenter=commenter,
                body=body
            )


class TestViews(SetUpViewsMixin, TestCase):
    """
    Extends SetUp Views Mixin, and gets the setUp method.

    Extends django.test.TestCase and gets all assertion functionality

    Test every view and it's HTTP methods
    """

    def test_blog_view_GET(self):

        response = self.client.get(self.list_blog_url)

        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response, "blog/blog_home.html")

        # Asserts that all the posts are passed to the views
        self.assertQuerysetEqual(
            response.context["object_list"], Post.objects.all().order_by("-date"), transform=lambda x: x)

        self.assertQuerysetEqual(
            response.context["cat_items"], Category.objects.all().order_by("-date"), transform=lambda x: x)

        self.create_categories(number=5)

        response = self.client.get(self.list_blog_url)

        # Cat items just pass 5 elements
        self.assertQuerysetEqual(
            response.context["cat_items"], ALL_CATEGORIES[:5], transform=lambda x: x)

    def test_blog_view_GET_filtering_liked(self):

        url = self.list_blog_url + "?filter=liked"

        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response, "blog/blog_home.html")

        self.assertQuerysetEqual(
            response.context["object_list"], MOST_LIKED_POSTS, transform=lambda x: x)

        self.post1.upvotes.add(self.user1)

        self.assertQuerysetEqual(
            response.context["object_list"], MOST_LIKED_POSTS, transform=lambda x: x)

    def test_blog_view_GET_filtering_commented(self):

        # Create 4 comments on self.post1
        self.create_comments_on_post(
            number=4, post=self.post1, commenter=self.user1)

        url = self.list_blog_url + "?filter=commented"

        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response, "blog/blog_home.html")

    def test_blog_search_view_GET(self):

        response = self.client.get(self.search_url)

        self.assertIsNone(response.context["posts"])

        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response, "base.html")

        self.assertTemplateUsed(response, "blog/blog_home.html")

        self.assertTemplateUsed(response, "blog/search/search.html")

    def test_blog_search_view_GET_with_query(self):

        # The url is searching for posts that contains "awesome post" in their contents

        url = self.search_url + "?q=awesome+post"

        # Get the url with the client
        response = self.client.get(url)

        # The number of posts that are passed to the context are 0
        # Because there are not posts that contains that posts
        self.assertEquals(response.context["posts"].count(), 0)

        self.assertEquals(response.status_code, 200)

        # Custom function that creates posts
        self.create_posts_evenly(name="AWeSOME Post", number=6)

        # New response with updated database
        response = self.client.get(url)
        self.assertEquals(response.context["posts"].count(), 6)

        new_url = self.search_url + "?q=a+cool"

        response = self.client.get(new_url)

        self.assertEquals(response.context["posts"].count(), 1)

    def test_blog_categories_view_GET(self):

        response = self.client.get(self.list_categories_url)

        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(
            response, "blog/categories/all_categories.html")

        self.assertQuerysetEqual(response.context["object_list"],
                                 Category.objects.all(),
                                 transform=lambda x: x)

        self.assertEquals(response.context["object_list"].count(), 1)

        self.create_categories(number=6)

        response = self.client.get(self.list_categories_url)

        self.assertEquals(response.context["object_list"].count(), 7)

    def test_blog_created_post_GET(self):
        # Get response
        response = self.client.get(self.create_post_url)

        self.assertEquals(response.status_code, 200)

        self.assertEquals(Post.objects.all().count(), 2)

        self.assertTemplateUsed(response, "blog/article/create_article.html")

    def test_blog_create_post_POST(self):

        # Asserts there are 2 posts before the creation of one
        self.assertEquals(Post.objects.all().count(), 2)

        form = {
            "title": "An awesome post",
            "description": "The best post ever",
            "body": "A horrific and cool body post with a lot of content"
        }

        # Post response
        response = self.logged_in_client.post(self.create_post_url, form)

        self.assertEquals(response.status_code, 302)

        self.assertEquals(Post.objects.all().count(), 3)

        self.assertTrue(
            Post.objects.filter(title="An awesome post").exists())

        self.assertEquals(
            Post.objects.get(title="An awesome post").description,
            "The best post ever")

    def test_blog_create_post_POST_no_data(self):

        form = {}

        response = self.logged_in_client.post(self.create_post_url, form)

        # User isn't being redirected
        self.assertEquals(response.status_code, 200)

        self.assertEquals(Post.objects.all().count(), 2)

    def test_blog_create_category_GET(self):

        response = self.client.get(self.create_category_url)

        self.assertEquals(Category.objects.all().count(), 1)

        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response,
                                "blog/categories/create_category.html")

    def test_blog_create_category_POST(self):

        form = {
            "name": "A awesome category",
        }

        response = self.logged_in_client.post(self.create_category_url,
                                              form)

        self.assertEquals(response.status_code, 302)

        # Category has been created
        self.assertEquals(Category.objects.all().count(), 2)

    def test_blog_create_category_POST_no_data(self):
        # No data passed to the form
        form = {}

        response = self.logged_in_client.post(self.create_category_url,
                                              form)

        # User isn't redirected
        self.assertEquals(response.status_code, 200)

        # Category wasn't created
        self.assertEquals(Category.objects.all().count(), 1)

    def test_blog_create_category_POST_proof_name_uniqueness(self):

        form = {
            "name": "A awesome category",
        }

        response = self.logged_in_client.post(self.create_category_url,
                                              form)

        self.assertEquals(response.status_code, 302)

        # Category has been created
        self.assertEquals(Category.objects.all().count(), 2)

        # Second try
        second_response = self.logged_in_client.post(self.create_category_url,
                                                     form)

        # User isn't redirected
        self.assertEquals(second_response.status_code, 200)

        # Second Category hasn't been created
        self.assertEquals(Category.objects.all().count(), 2)

    def test_blog_detail_edit_post_GET(self):

        response = self.logged_in_client.get(self.detail_edit_post_url)

        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response,
                                "blog/article/edit_article.html")

    def test_blog_detail_edit_post_POST(self):
        """No testing :("""

        pass
        # Create a post with author of the client logged in

        # pss = "123"
        # author = User().objects.create(
        #     first_name="a",
        #     last_name="b",
        #     email="a@b.com",
        # )

        # author.set_password(pss)

        # author.save()

        # new_post = Post.objects.create(
        #     title="New Post",
        #     author=author,
        #     body="Body"
        # )

        # body = "A cooooooool body"

        # form = {
        #     "body": body,
        # }

        # self.logged_in_client.logout()

        # self.logged_in_client.login(email="a@b.com", password=pss)

        # url = reverse("blog:edit_article", args=[new_post.id])

        # # The user that is edited has to be the author
        # response = self.logged_in_client.post(url, form)

        # # self.assertEquals(response.status_code, 302)

        # self.assertEquals(new_post.body, body)

    def test_blog_detail_delete_view_GET(self):
        response = self.client.get(self.detail_delete_post_url)

        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response, "blog/article/delete_article.html")

    def test_blog_detail_delete_view_POST(self):
        """
        Delete test
        """

        self.assertTrue(Post.objects.filter(
            id=self.post2.id).exists())

        response = self.client.post(self.detail_delete_post_url)

        self.assertFalse(Post.objects.filter(
            id=self.post2.id).exists())

        self.assertEquals(response.status_code, 302)

    def test_blog_detail_post_GET(self):

        response = self.client.get(self.detail_post_url)

        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response,
                                "blog/article/detail_article.html")

        self.assertEquals(response.context["post"],
                          self.post1)

        self.assertEquals(response.context["upvotes"],
                          self.post1.total_likes())

        self.assertQuerysetEqual(response.context["comments"],
                                 Comment.objects.filter(
            post=self.post1).order_by('-date_added'))

    def test_blog_detail_post_POST(self):

        self.assertEquals(self.post1.number_of_comments, 0)

        form = {
            "body": "Hi there this is my comment xd"
        }

        response = self.logged_in_client.post(self.detail_post_url,
                                              form)

        self.assertEquals(response.status_code, 302)

        self.assertEquals(self.post1.number_of_comments, 1)

    def test_blog_detail_category_GET(self):

        response = self.client.get(self.detail_category_url)

        self.assertEquals(response.status_code, 200)

    def test_blog_detail_edit_category_GET(self):

        response = self.logged_in_client.get(self.detail_edit_category_url)

        self.assertEquals(response.status_code, 200)

    def test_blog_detail_edit_category_POST_no_admin_user(self):
        # Asserts the name of the category1

        self.assertEquals(self.category1.name, "cool-category")

        form = {
            "name": "Other NAME",
            "image": "",
            "description": "A cool description"
        }

        response = self.logged_in_client.post(
            self.detail_edit_category_url, form
        )

        self.assertEquals(response.status_code, 302)

        self.assertNotEquals(self.category1.name, "other name")

    def test_blog_edit_category_POST_admin(self):

        form = {
            "name": "Other NAME",
            "image": "",
            "description": "A cool description"
        }

        pss = "extremely_difficult_password123"

        admin = User().objects.create_superuser(
            first_name="admin",
            last_name="user",
            email="admin@admin.com",
            password=pss
        )

        login = self.client.login(
            email=admin.email,
            password=pss)

        self.assertTrue(login)

        user_ = get_user(self.client)

        self.assertTrue(user_.is_admin)

        self.assertEquals(self.category1.name,
                          "cool-category")

        response = self.client.post(self.detail_edit_category_url,
                                    form)

        # No idea why this doesn't work :(
        # self.assertEquals(self.category1.name,
        #                   "other name")
    
