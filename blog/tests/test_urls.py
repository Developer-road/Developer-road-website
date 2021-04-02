from django.test import SimpleTestCase

# Create your tests here.

from django.urls import reverse, resolve

from blog.views import (BlogView,
                        ArticleDetail,
                        PostCreateView,
                        EditPost,
                        PostDeleteView,
                        CategoryCreateView,
                        CategoryUpdateView,
                        CategoryView,
                        CategoryListView,
                        VoteView,
                        BlogSearchView,
                        )


class TestBlogUrls(SimpleTestCase):

    #############################
    #        No argument        #
    #############################

    #############################
    #        Listing tests      #
    #############################

    def test_home_blog_page_resolves(self):

        url = reverse("blog:home")

        # Asserts that the url points to:
        # class based view: BlogView

        self.assertEquals(
            resolve(url).func.view_class,
            BlogView)

    def test_search_post_resolves(self):

        url = reverse("blog:search")

        # Asserts that the url points to:
        # class based view: BlogSearchView

        self.assertEquals(
            resolve(url).func.view_class,
            BlogSearchView)

    def test_list_category_resolves(self):

        url = reverse("blog:categories")

        self.assertEquals(
            resolve(url).func.view_class,
            CategoryListView
        )


    #############################
    #        Create tests      #
    #############################

    def test_create_post_resolves(self):

        url = reverse("blog:create_article")

        self.assertEquals(
            resolve(url).func.view_class,
            PostCreateView
        )

    def test_create_category_resolves(self):

        url = reverse("blog:create_category")

        self.assertEquals(
            resolve(url).func.view_class,
            CategoryCreateView
        )

    ###############################
    #         With argument       #
    ###############################

    ###############################
    #         Detail Tests        #
    ###############################

    def test_detail_post_resolves(self):

        # parameter: blog pk
        url = reverse("blog:article", args=[1])

        # Asserts that the url points to:
        # class based view: BlogView

        self.assertEquals(url, "/blog/article/1/")

        self.assertEquals(
            resolve(url).func.view_class,
            ArticleDetail)

    def test_detail_category_resolves(self):

        url = reverse("blog:category", args=["some-cat"])

        self.assertEquals(url, "/blog/category/some-cat/")

        self.assertEquals(
            resolve(url).func.view_class,
            CategoryView
        )

    def test_detail_upvotes_resolves(self):

        url = reverse("blog:upvotes",
                      args=[2])

        self.assertEquals(url, "/blog/upvotes/2/")

        self.assertEquals(
            resolve(url).func,
            VoteView
        )

    ###############################
    #         Edit Tests        #
    ###############################

    def test_edit_detail_post_resolves(self):

        url = reverse("blog:edit_article", args=[1])

        self.assertEquals(url, "/blog/article/1/edit/")
        self.assertEquals(
            resolve(url).func.view_class,
            EditPost
        )

    def test_detail_edit_category_resolves(self):

        url = reverse("blog:edit_category", args=[2])

        self.assertEquals(url, "/blog/category/2/edit/")

        self.assertEquals(
            resolve(url).func.view_class,
            CategoryUpdateView
        )

    ###############################
    #         Delete Tests        #
    ###############################

    def test_detail_delete_post_resolves(self):

        url = reverse("blog:delete_article", args=[1])

        self.assertEquals(url, "/blog/article/1/delete/")

        self.assertEquals(
            resolve(url).func.view_class,
            PostDeleteView
        )
