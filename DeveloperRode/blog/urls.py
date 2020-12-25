from django.urls import path
from .views import BlogView, ArticleDetail

app_name = 'blog'
urlpatterns = [
    path('', BlogView.as_view(), name="blog_page"),
    path('article/<int:pk>', ArticleDetail.as_view(), name="article_page"),
]
