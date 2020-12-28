from django.urls import path
from .views import BlogView, ArticleDetail, PostCreateView

app_name = 'blog'
urlpatterns = [
    path('', BlogView.as_view(), name="blog_page"),
    path('article/<int:pk>', ArticleDetail.as_view(), name="article_page"),
    path('create/', PostCreateView.as_view(), name="add_post"),
]
