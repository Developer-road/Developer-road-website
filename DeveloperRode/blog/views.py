from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
# Import the Post object
from .models import Post


# Create your views here.
class BlogView(ListView):
    model = Post
    template_name = 'blog/index.html'

class ArticleDetail(DetailView):
    model = Post
    template_name = 'blog/details.html'