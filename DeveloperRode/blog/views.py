from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
# Import the Post object

from .models import Post

from .forms import PostForm, EditForm

from django.urls import reverse_lazy
# Create your views here.
class BlogView(ListView):
    """
    View that shows the list of all the existent blogs
    """
    model = Post
    template_name = 'blog/index.html'
    ordering = ["-date"]


class ArticleDetail(DetailView):
    """
    View that shows in detail the chosen blog post.
    """
    model = Post
    template_name = 'blog/details.html'

class PostCreateView(CreateView):
    """
    Used to create a brand new blog post
    """
    
    model = Post
    form_class = PostForm
    template_name = "blog/add_post.html"
    # fields = "__all__"


class EditPost(UpdateView):
    """
    Used to edit an existing blog post
    """

    model = Post
    template_name = 'blog/edit_post.html'
    form_class = EditForm
    # fields = ('title','meta_description', 'body')

class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy("blog:blog_page")
