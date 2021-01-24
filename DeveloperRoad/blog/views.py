from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView
from django.views import View
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.db.models import Q

# Import the Post object and Category object

from .models import Post, Category, Comment

from .forms import PostForm, EditPostForm, CreateCategoryForm, CommentForm


class BlogView(ListView):
    """
    View that shows the list of all the existent blogs
    """
    model = Post
    queryset = Post.objects.order_by('-date')
    paginate_by = 4
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat_items"] = Category.objects.all()

        return context


class BlogSearchView(ListView):
    """
    View that shows the list of all the existent blogs
    """
    model = Post
    # queryset = Post.objects.order_by('-date')

    paginate_by = 4
    template_name = 'blog/search.html'

    def get_queryset(self):  # new
        if "q" in self.request.GET:
            query = self.request.GET.get('q')
            object_list = Post.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
            return object_list
        else:
            object_list = None
            return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat_items"] = Category.objects.all()

        return context


class ArticleDetail(DetailView):
    """
    View that shows in detail the chosen blog post.
    """
    model = Post
    template_name = 'blog/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        detail_post = get_object_or_404(Post, id=self.kwargs['pk'])
        context["upvotes"] = detail_post.total_likes()
        upvoted = False

        if detail_post.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True

        context["upvoted"] = upvoted

        try:
            context["comments"] = list(Comment.objects.filter(
                post_id=detail_post.id).order_by('-date_added'))
        except:
            context["comments"] = None

        if self.request.user.is_authenticated:
            context["comment_form"] = CommentForm(instance=self.request.user)

        return context

    def post(self, request, *args, **kwargs):
        new_comment = Comment(body=request.POST.get('body'),
                              commenter=self.request.user,
                              post=self.get_object())
        new_comment.save()
        return HttpResponseRedirect(reverse('blog:article_page', args=[str(self.kwargs['pk'])]))


class PostCreateView(CreateView):
    """
    Used to create a brand new blog post
    """

    model = Post
    form_class = PostForm
    template_name = "blog/add_post.html"
    # fields = "__all__"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


class CategoryView(View):
    """
    Display a category page
    """

    def get(self, request, cat):

        category_name = get_object_or_404(Category, name=cat.replace("-", " "))

        try:
            category_post = list(Post.objects.filter(
                category_id=category_name.id))
        except Post.DoesNotExist:
            category_post = None

        
        context = {"category_name": category_name,
                   "category_post": category_post,
                   "category_hidden": True}
        return render(request, "blog/categories.html", context)


class CategoryListView(ListView):
    model = Category
    template_name = "blog/categories_list.html"


class CategoryCreateView(CreateView):
    """
    Used to create a new blog category
    """

    model = Category
    # fields = "__all__"
    form_class = CreateCategoryForm
    template_name = "blog/add_category.html"


class EditPost(UpdateView):
    """
    Used to edit an existing blog post
    """

    model = Post
    template_name = 'blog/edit_post.html'
    form_class = EditPostForm
    # fields = ('title','meta_description', 'body')


class PostDeleteView(DeleteView):
    """
    Used to Delete A post
    """
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy("blog:blog_page")


def VoteView(request, pk):
    post = Post.objects.get(id=pk)

    if post.upvotes.filter(id=request.user.id).exists():
        post.upvotes.remove(request.user)
    else:
        post.upvotes.add(request.user)
    return HttpResponseRedirect(reverse('blog:article_page', args=[str(pk)]))
