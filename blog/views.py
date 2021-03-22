from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView, FormView
from django.views import View
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Search functionality
from django.db.models import Q


from django.db.models import Count

# Import the Post object and Category object

from .models import Post, Category, Comment

from .forms import PostForm, EditPostForm, CreateCategoryForm, CommentForm



ALL_CATEGORIES = Category.objects.all()

class BlogView(ListView):
    """
    View that shows the list of all the newest
    """
    model = Post
    queryset = Post.objects.order_by('-date')
    paginate_by = 6
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat_items"] = ALL_CATEGORIES

        return context

class BlogMostLikedView(ListView):
    """
    View that shows the list of all the existent blogs
    """
    model = Post
    queryset = Post.objects.annotate(most_liked=Count("upvotes")).order_by('-most_liked')
    paginate_by = 6
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat_items"] = ALL_CATEGORIES

        return context



class BlogSearchView(ListView):
    """
    View that shows the list of all the existent blogs
    """
    model = Post
    # queryset = Post.objects.order_by('-date')

    # paginate_by = 4
    template_name = 'blog/search.html'

    def get_queryset(self):  # new
        if "q" in self.request.GET:
            if str(self.request.GET.get('q')) not in ["", " "]:
                query = self.request.GET.get('q')
                object_list = Post.objects.filter(
                    Q(title__icontains=query) | Q(
                        description__icontains=query) | Q(body__icontains=query)
                ).distinct().order_by("-date")
            else:
                object_list = None
            return object_list
        else:
            object_list = None
            return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat_items"] = Category.objects.all()

        query = "No search"
        if "q" in self.request.GET:
            query = str(self.request.GET.get('q'))
        context["string_query"] = query

        return context


class ArticleDetail(CreateView):
    """
    View that shows in detail the chosen blog post.
    """
    model = Comment
    form_class = CommentForm

    template_name = 'blog/details.html'

    def get_detail_post(self):

        return get_object_or_404(Post, id=self.kwargs['pk'])

    # Redirects when the comment is created

    def get_success_url(self, *args, **kwargs):
        
        return reverse('blog:article_page', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        detail_post = self.get_detail_post()

        # Pass the detail post as the object
        context["post"] = detail_post

        # Calls the Post property of counting the upvotes of the post
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

        recent = True
        other_posts = Post.objects.all().order_by('-date')[:4]

        if detail_post.category:
            # If the post has a category, related posts are from the category

            related_posts = list(Post.objects.filter(
                category=detail_post.category))

            # We have to take into account the same post

            if len(related_posts) > 1:
                other_posts = related_posts
                recent = False

        context["recent"] = recent
        context["other_posts"] = other_posts

        return context

    # Validate the form with the user, and post
    def form_valid(self, form):

        detail_post = self.get_detail_post()

        user = self.request.user

        form.instance.commenter = user

        form.instance.post = detail_post

        return super().form_valid(form)


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

        # Custom slug name
        # Terrible decision by the way

        category_name = get_object_or_404(Category, name__iexact=cat.replace("-", " "))

        try:
            category_post = Post.objects.filter(
                category_id=category_name.id).order_by("-date")
        except Post.DoesNotExist:
            category_post = None

        context = {}

        context["category_name"] = category_name

        context["category_post"] = category_post

        # This is to don't show the category link
        context["category_hidden"] = True

        return render(request, "blog/categories.html", context)


class CategoryListView(ListView):

    model = Category

    queryset = Category.objects.annotate(
        post_count=Count('post')).order_by("-post_count")

    template_name = "blog/categories_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Excluded Pre created categories that has as image field None
        categories_created_before_image_migration = Category.objects.exclude(
            image=None)        

        # Excluded Categories created after image field migration but without image

        categories_created_without_images = Category.objects.exclude(
            image="")

        # Intersection between these two querysets

        context["categories_with_image"] = categories_created_before_image_migration.intersection(categories_created_without_images)

        return context
    

class CategoryCreateView(CreateView):
    """
    Used to create a new blog category
    """

    model = Category

    form_class = CreateCategoryForm

    template_name = "blog/add_category.html"


    def get_success_url(self, *args, **kwargs):
        
        return reverse_lazy('blog:categories_page')

    

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = "blog/edit_category.html"
    
    def get_success_url(self, *args, **kwargs):
        
        return reverse_lazy('blog:categories_page')


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
