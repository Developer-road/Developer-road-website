"""Base views for categories model"""

# Django

from django.shortcuts import get_object_or_404

# Urls
from django.urls import reverse_lazy

from django.views.generic import (
    View,
    DetailView,
    ListView,
)


# Search functionality
from django.db.models import Q
from django.db.models import Count

# Utilities
from blog.utils import ALL_CATEGORIES

# Import the Post object and Category object
from blog.models import (
    Category,
    Post,
)

from blog.forms import (
    CreateCategoryForm,
    EditCategoryForm,
)


class BaseCategoryData:

    model = Category

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('blog:categories')


class BaseEditCategoryData(BaseCategoryData):

    form_class = EditCategoryForm

    template_name = "blog/categories/edit_category.html"


class BaseCreateCategoryData(BaseCategoryData):

    form_class = CreateCategoryForm

    template_name = "blog/categories/create_category.html"


class BaseCategoryView(View):
    """
    Base category view

    Base functions for getting the contexts
    """

    def get_category(self, request, slug):

        category_name = slug.replace("-", " ")

        category = get_object_or_404(Category,
                                     name__iexact=category_name)

        return category

    def get_category_posts(self, request, slug):

        try:
            return Post.objects.filter(
                category=self.get_category(request, slug)
            )

        except Post.DoesNotExist:
            return None

    def get_category_and_posts(self, request, slug):
        """
        Returns the category and it's posts
        """

        return self.get_category(request, slug), self.get_category_posts(request, slug)


class BaseCategoryListView(ListView):

    """
    Base Category List View

    List all the categories ordered by number of posts

    """

    model = Category

    queryset = ALL_CATEGORIES
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Excluded Pre created categories that has as image field None
        categories_created_before_image_migration = Category.objects.exclude(
            image=None)

        # Excluded Categories created after image field migration but without image

        categories_created_without_images = Category.objects.exclude(
            image="")

        # Intersection between these two querysets

        context["categories_with_image"] = categories_created_before_image_migration.intersection(
            categories_created_without_images)

        return context