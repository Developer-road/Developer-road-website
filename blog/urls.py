from django.urls import path
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
                    BlogMostLikedView)

app_name = 'blog'


urlpatterns = [
    # Default blog home page
    path('',
         BlogView.as_view(),
         name="blog_page"),

    # Filtered most like blog page
    path('liked/',
         BlogMostLikedView.as_view(),
         name="blog_liked_page"),

    # Detail url of a blog post
    # parameter: pk of a blog post
    path('article/<int:pk>/',
         ArticleDetail.as_view(),
         name="article_page"),

    # Edit page of a blog post,
    # parameter: primary key of a blog post
    path('article/<int:pk>/edit/',
         EditPost.as_view(),
         name="edit_page"),

    # Delete page of a blog post,
    # only the creator can delete the post
    # parameter: pk of the blog post
    path('article/<int:pk>/delete/',
         PostDeleteView.as_view(),
         name="delete_page"),

    # Create page for a blog post
    path('create/',
         PostCreateView.as_view(),
         name="add_post"),

    # Create category page,
    # only logged users can create one
    path('create_category/',
         CategoryCreateView.as_view(),
         name="add_category"),

    # List all the categories
    path('categories/',
         CategoryListView.as_view(),
         name="categories_page"),

    # Detail category view
    # parameter: the category name
    path('category/<str:cat>/',
         CategoryView.as_view(),
         name="category_page"),

    # Category edit page
    # parameter: pk of category
    path('category/<int:pk>/edit/',
         CategoryUpdateView.as_view(),
         name="category_edit"),

    # Upvotes category handler
    # Function view that adds an upvote to the blog post
    # parameter: Blog post pk
    path('upvotes/<int:pk>/',
         VoteView,
         name="upvotes"),

    # Search stuff
    path('search/',
         BlogSearchView.as_view(),
         name="search"),
]
