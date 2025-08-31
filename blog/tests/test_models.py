from django.test import TestCase

from django.urls import reverse, resolve

from django.core.files.uploadedfile import SimpleUploadedFile

from django.contrib.auth import get_user_model

from blog.models import (
    Post,
    Category,
    Comment,
)

from blog.utils import SMALL_GIF, SIMPLE_IMAGE

class TestCategoryModel(TestCase):

    def setUp(self):
        """
        Create 3 categories, one only with name,
        the second with name and description, and the last
        with name, description and image
        """

        self.category1 = Category.objects.create(
            name="category1",
        )

        self.category2 = Category.objects.create(
            name="category2",
            description="This category has a description"
        )

        # Creates and image for the category3
        # It uploads to media folder when test is runned
        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=SIMPLE_IMAGE,
            content_type='image/jpeg'
        )

        self.category3 = Category.objects.create(
            name="category3",
            description="A cool category with image",
            image=self.test_image
        )

    def test_category_image(self):
        """
        Tests that the image functionality is working.
        And the uploads are being sended to the media folder
        """

        self.assertEqual(self.category1.image, None)

        self.assertEqual(self.category2.image, None)

        self.assertNotEqual(self.category3.image, None)

        self.assertTrue(self.category3.image.url.startswith(
            "/media/images/categories/test"))

    def test_category_description(self):
        """
        Test that the given description is being correctly assigned
        """

        self.assertNotEqual(self.category1.description, None)

        self.assertEqual(self.category1.description,
                          "This category hasn't a description yet")

        self.assertNotEqual(self.category2.description,
                             "This category hasn't a description yet")

        self.assertNotEqual(self.category3.description,
                             "This category hasn't a description yet")

    def test_absolute_url(self):
        """
        Test that the absolute url, is pointing to the
        detail category page, and pass as argument the lowercase and hypens replaced name
        """

        spaces_category = Category.objects.create(
            name="A cool category Xd"
        )

        self.assertEqual(
            self.category1.get_absolute_url(),
            reverse("blog:category", args=["category1"])
        )

        self.assertEqual(
            spaces_category.get_absolute_url(),
            reverse("blog:category", args=["a-cool-category-xd"])
        )

    def test_property_number_of_category_posts_NO_POSTS(self):
        """
        Test that the category has the right number of posts assigned
        """
        self.assertEqual(self.category1.number_of_category_posts, 0)
        self.assertEqual(self.category2.number_of_category_posts, 0)
        self.assertEqual(self.category3.number_of_category_posts, 0)

    def test_property_number_of_category_posts_WITH_POSTS(self):

        user = get_user_model().objects.create(
            email="user@user.com",
            first_name="user",
            last_name="last",
            password="user_pass"
        )

        Post.objects.create(
            title="A cool Post",
            author=user,
            category=self.category1,
            body="Hi there"
        )

        self.assertEqual(self.category1.number_of_category_posts, 1)
        self.assertEqual(self.category2.number_of_category_posts, 0)


class SetUpPostAndCommentMixin(object):
    def setUp(self):
        self.user1 = get_user_model().objects.create(
            email="user1@gmail.com",
            first_name="user",
            last_name="Last name",
            password="user1password"
        )

        self.user2 = get_user_model().objects.create(
            email="user2@gmail.com",
            first_name="user",
            last_name="Last name",
            password="user2password"
        )

        self.post1 = Post.objects.create(
            title="Post 1",
            author=self.user1,
            body="A cool post"
        )

        self.post2 = Post.objects.create(
            title="Post 2",
            author=self.user2,
            body="A cool post 2"
        )

        self.comment1 = Comment.objects.create(
            post=self.post1,
            commenter=self.user1,
            body="A cool comment 1"
        )

        self.comment2 = Comment.objects.create(
            post=self.post2,
            commenter=self.user2,
            body="A cool comment 2"
        )

        self.category1 = Category.objects.create(
            name="category1",
            description="A cool description"
        )


class TestCommentModel(SetUpPostAndCommentMixin, TestCase):
    def test_comment_post_assignment(self):

        # Test the comment 1 is only assigned to post 1
        self.assertEqual(self.comment1.post, self.post1)

        self.assertNotEqual(self.comment1.post, self.post2)

        # Test the comment 2 is only assigned to post 2
        self.assertEqual(self.comment2.post, self.post2)

        self.assertNotEqual(self.comment2.post, self.post1)

    def test_comment_post_DELETE_on_cascade(self):

        comment1_id = self.comment1.id

        # Asserts that the comment exist

        self.assertTrue(Comment.objects.filter(id=comment1_id).exists())

        self.post1.delete()

        # Assert that the comment is deleted when the post is deleted
        self.assertFalse(Comment.objects.filter(id=comment1_id).exists())

    def test_comment_commenter_DELETE_on_cascade(self):

        commenter1 = self.comment1.commenter
        commenter1_id =  commenter1.id # PK (Django 5.x + requiered now)

        # Asserts that the comment exist if the use exists
        self.assertTrue(Comment.objects.filter(commenter=commenter1).exists())

        self.user1.delete()
        # Asserts that the comment doesn't exist when the user has been deleted
        self.assertFalse(Comment.objects.filter(commenter_id=commenter1_id).exists())


class TestPostModel(SetUpPostAndCommentMixin, TestCase):

    def setUp(self):
        super().setUp()

        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=SMALL_GIF,
            content_type='image/jpeg'
        )

        self.image_post = Post.objects.create(
            title="Image Post",
            description="Hi there this is a Image Post",
            author=self.user1,
            category=self.category1,
            header_image=self.test_image
        )

    def test_well_assigned_title(self):
        self.assertEqual(self.image_post.title, "Image Post")

    def test_post_author_DELETE_on_cascade(self):

        post_id = self.image_post.id

        self.assertTrue(Post.objects.filter(id=post_id).exists())

        self.user1.delete()

        self.assertFalse(Post.objects.filter(id=post_id).exists())

    def test_post_author_email(self):

        self.assertEqual(self.image_post.author.email, "user1@gmail.com")

    def test_header_image_on_creation(self):

        self.assertEqual(self.post1.header_image, None)

        self.assertEqual(self.post2.header_image, None)

        self.assertNotEqual(self.image_post.header_image, None)

        self.assertTrue(self.image_post.header_image.url.startswith(
            "/media/images/post_header/test_"))

    def test_well_assigned_description(self):

        self.assertIsNone(self.post1.description)
        self.assertIsNone(self.post2.description)

        self.assertEqual(self.image_post.description,
                          "Hi there this is a Image Post")

    def test_post_category_DELETE_set_null(self):

        test_category = Category.objects.create(
            name="category-test"
        )

        test_post = Post.objects.create(
            title="Test project",
            author=self.user1,
            category=test_category,
            body="Some body"
        )

        test_category_id = test_category.id

        self.assertEqual(test_post.category, test_category)

        self.assertTrue(Post.objects.filter(
            category__id=test_category_id).exists())

        test_category.delete()

        # Since now the category1 doesn't exist the filtered object return False
        self.assertFalse(Post.objects.filter(
            category__id=test_category_id).exists())

        self.assertTrue(Post.objects.filter(id=test_post.id).exists())

    def test_post_upvotes_count(self):

        self.assertEqual(self.image_post.upvotes.count(), 0)
        self.assertEqual(self.post1.upvotes.count(), 0)
        self.assertEqual(self.post2.upvotes.count(), 0)

        self.image_post.upvotes.add(self.user1)

        self.assertEqual(self.image_post.upvotes.count(), 1)

        self.post1.upvotes.add(self.user1, self.user2)

        self.assertEqual(self.post1.upvotes.count(), 2)

        self.post1.upvotes.remove(self.user1)

        self.assertEqual(self.post1.upvotes.count(), 1)

        self.user2.delete()

        self.assertEqual(self.post1.upvotes.count(), 0)

    ###########################
    #    Testing properties   #
    ###########################

    def testing_total_likes(self):

        self.assertEqual(self.post1.total_likes(), 0)

        self.post1.upvotes.add(self.user1)

        self.assertEqual(self.post1.total_likes(), 1)

    def test_post_get_absolute_url(self):
        Cool_post = Post.objects.create(
            title="A cool post xd",
            body="Body",
            author=self.user1
        )

        post_id = Cool_post.id

        self.assertEqual(
            Cool_post.get_absolute_url(),
            reverse("blog:article", args=[post_id])
        )

        self.assertEqual(
            Cool_post.get_absolute_url(),
            reverse("blog:article", args=[post_id])
        )

        self.assertEqual(
            Cool_post.get_absolute_url(),
            f"/blog/article/{post_id}/"
        )

    def test_post_number_of_comments_property(self):
        
        self.assertEqual(self.post1.number_of_comments, 1)
        self.assertEqual(self.post2.number_of_comments, 1)

        Comment.objects.create(
            post=self.post1,
            commenter=self.user1,
            body="A comment xd"
        )

        self.assertEqual(self.post1.number_of_comments, 2)
