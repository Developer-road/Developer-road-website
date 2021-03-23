from django.test import TestCase

from django.urls import reverse, resolve

from django.core.files.uploadedfile import SimpleUploadedFile

from django.contrib.auth import get_user_model

from blog.models import (
    Post,
    Category,
    Comment,
)

SMALL_GIF = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
    b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
    b'\x02\x4c\x01\x00\x3b'
)


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
            content=b"Lets grab a \xf0\x9f\x8d\x95!",
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

        self.assertEquals(self.category1.image, None)

        self.assertEquals(self.category2.image, None)

        self.assertNotEquals(self.category3.image, None)

        self.assertTrue(self.category3.image.url.startswith(
            "/media/images/categories/test"))

    def test_category_description(self):
        """
        Test that the given description is being correctly assigned
        """

        self.assertNotEquals(self.category1.description, None)

        self.assertEquals(self.category1.description,
                          "This category hasn't a description yet")

        self.assertNotEquals(self.category2.description,
                             "This category hasn't a description yet")

        self.assertNotEquals(self.category3.description,
                             "This category hasn't a description yet")

    def test_absolute_url(self):
        """
        Test that the absolute url, is pointing to the
        detail category page, and pass as argument the lowercase and hypens replaced name
        """

        spaces_category = Category.objects.create(
            name="A cool category Xd"
        )

        self.assertEquals(
            self.category1.get_absolute_url(),
            reverse("blog:category_page", args=["category1"])
        )

        self.assertEquals(
            spaces_category.get_absolute_url(),
            reverse("blog:category_page", args=["a-cool-category-xd"])
        )

    def test_property_number_of_category_posts_NO_POSTS(self):
        """
        Test that the category has the right number of posts assigned
        """
        self.assertEquals(self.category1.number_of_category_posts, 0)
        self.assertEquals(self.category2.number_of_category_posts, 0)
        self.assertEquals(self.category3.number_of_category_posts, 0)

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

        self.assertEquals(self.category1.number_of_category_posts, 1)
        self.assertEquals(self.category2.number_of_category_posts, 0)






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



class TestCommentModel(SetUpPostAndCommentMixin,TestCase):
    def test_comment_post_assignment(self):

        # Test the comment 1 is only assigned to post 1
        self.assertEquals(self.comment1.post, self.post1)

        self.assertNotEquals(self.comment1.post, self.post2)

        # Test the comment 2 is only assigned to post 2
        self.assertEquals(self.comment2.post, self.post2)

        self.assertNotEquals(self.comment2.post, self.post1)

    def test_comment_post_DELETE_on_cascade(self):

        comment1_id = self.comment1.id

        # Asserts that the comment exist

        self.assertTrue(Comment.objects.filter(id=comment1_id).exists())

        self.post1.delete()

        # Assert that the comment is deleted when the post is deleted
        self.assertFalse(Comment.objects.filter(id=comment1_id).exists())

    def test_comment_commenter_DELETE_on_cascade(self):

        commenter1 = self.comment1.commenter

        # Asserts that the comment exist if the use exists
        self.assertTrue(Comment.objects.filter(commenter=commenter1).exists())

        self.user1.delete()
        # Asserts that the comment doesn't exist when the user has been deleted
        self.assertFalse(Comment.objects.filter(commenter=commenter1).exists())

class TestPostModel(SetUpPostAndCommentMixin, TestCase):

    def setUp(self):
        super().setUp()


        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=SMALL_GIF,
            content_type='image/jpeg'
        )


        


