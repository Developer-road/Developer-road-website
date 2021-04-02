"""Blog Views"""

# Django
from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


# All Categories
from .utils import ALL_CATEGORIES

from .base_views import *


class BlogView(BaseBlogListView):
    """
    View that shows the list of all the newest blog posts
    """


class BlogSearchView(BaseBlogSearchView):
    """
    View that shows the list of all the newest blog posts
    """

    template_name = "blog/search/search.html"


class ArticleDetail(BaseArticleDetailView):
    """
    View that shows in detail the chosen blog post.
    """

    template_name = 'blog/article/detail_article.html'

class CategoryView(BaseCategoryView):
    """
    Display a category page

    Takes from the url the name with hypens and gets the object from the database
    """

    def get(self, request, slug):

        context = {}

        context["category_name"], context["category_post"] = self.get_category_and_posts(request, slug)

        context["category_hidden"] = True

        return render(request, "blog/categories/detail_category.html", context)

class CategoryListView(BaseCategoryListView):
    """ 
    View that renders the list of all categories

    order: Number of posts
    """

    template_name = "blog/categories/all_categories.html"


class CategoryCreateView(BaseCreateCategoryData, CreateView):
    """
    Used to create a new blog category

    Extends BaseCreateCategoryData for data, and CreateView for functionality

    Validation: Cannot create a category with the same name
    """


class CategoryUpdateView(BaseEditCategoryData, UpdateView):
    """
    View that updates the category model

    Extends BaseCreateCategoryData for data, and CreateView for functionality
    """


class PostCreateView(BaseCreatePostView):
    """
    Used to create a brand new blog post
    """

    template_name = "blog/article/create_article.html"



class EditPost(BaseEditPostView):
    """
    Used to edit an existing blog post
    """
    template_name = 'blog/article/edit_article.html'


class PostDeleteView(BaseDeletePostView):
    """
    Used to Delete A post
    """
    template_name = "blog/article/delete_article.html"