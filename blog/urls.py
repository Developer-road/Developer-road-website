"""
Blog Urls
"""

# Django
from django.urls import path

# Views
from .views import (BlogView,
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

app_name = 'blog'


urlpatterns = [
    # Default blog home page
    # Main url, accepts filter=liked
    path('',
         BlogView.as_view(),
         name="home"),

    path('search/',
         BlogSearchView.as_view(),
         name="search"),

    # Detail url of a blog post
    # parameter: pk of a blog post
    path('article/<int:pk>/',
         ArticleDetail.as_view(),
         name="article"),

    # Edit page of a blog post,
    # parameter: primary key of a blog post
    path('article/<int:pk>/edit/',
         EditPost.as_view(),
         name="edit_article"),

    # Delete page of a blog post,
    # only the creator can delete the post
    # parameter: pk of the blog post
    path('article/<int:pk>/delete/',
         PostDeleteView.as_view(),
         name="delete_article"),

    # Create page for a blog post
    path('create/',
         PostCreateView.as_view(),
         name="create_article"),

    # Create category page,
    # only logged users can create one
    path('create_category/',
         CategoryCreateView.as_view(),
         name="create_category"),

    # List all the categories
    path('categories/',
         CategoryListView.as_view(),
         name="categories"),

    # Detail category view
    # parameter: the category name
    path('category/<str:cat>/',
         CategoryView.as_view(),
         name="category"),

    # Category edit page
    # parameter: pk of category
    path('category/<int:pk>/edit/',
         CategoryUpdateView.as_view(),
         name="edit_category"),

    # Upvotes category handler
    # Function view that adds an upvote to the blog post
    # parameter: Blog post pk
    path('upvotes/<int:pk>/',
         VoteView,
         name="upvotes"),
]
