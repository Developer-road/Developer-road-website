from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
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

class PostCreateView(CreateView):
    model = Post
    template_name = "blog/add_page.html"
    fields = "__all__"
