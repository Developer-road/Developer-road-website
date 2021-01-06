from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy


# Import the Post object and Category object

from .models import Post, Category

from .forms import PostForm, EditForm


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


class CategoryView(View):
    """
    Display a category page
    """

    def get(self, request, cat):
        
        category_name = get_object_or_404(Category, name=cat.replace("-", " "))
        
        category_post = get_list_or_404(Post, category_id=category_name.id)
        context = {"category_name": category_name,
                   "category_post": category_post}
        return render(request, "blog/categories.html", context)


class CategoryCreateView(CreateView):
    """
    Used to create a new blog category
    """

    model = Category
    fields = "__all__"
    # form_class = PostForm
    template_name = "blog/add_category.html"


class EditPost(UpdateView):
    """
    Used to edit an existing blog post
    """

    model = Post
    template_name = 'blog/edit_post.html'
    form_class = EditForm
    # fields = ('title','meta_description', 'body')


class PostDeleteView(DeleteView):
    """
    Used to Delete A post
    """
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy("blog:blog_page")
