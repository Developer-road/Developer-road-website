from django.urls import path
from .views import BlogView, ArticleDetail, PostCreateView, EditPost, PostDeleteView, CategoryCreateView, CategoryView, CategoryListView

app_name = 'blog'
urlpatterns = [
    path('', BlogView.as_view(), name="blog_page"),
    path('article/<int:pk>', ArticleDetail.as_view(), name="article_page"),
    path('article/edit/<int:pk>', EditPost.as_view(), name="edit_page"),
    path('article/<int:pk>/delete', PostDeleteView.as_view(), name="delete_page"),
    path('create/', PostCreateView.as_view(), name="add_post"),
    path('create_category/', CategoryCreateView.as_view(), name="add_category"),
    path('categories/', CategoryListView.as_view(), name="categories_page"),
    path('category/<str:cat>/', CategoryView.as_view(), name="category_page"),
]
