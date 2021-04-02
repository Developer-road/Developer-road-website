"""
Base Views for Blog Views
"""

# Django

from django.shortcuts import get_object_or_404

from django.urls import reverse_lazy, reverse

from django.http import HttpResponseRedirect

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)


# Search functionality
from django.db.models import Q
from django.db.models import Count


from blog.utils import ALL_CATEGORIES

# Import the Post object and Category object
from blog.models import (
    Post,
    Comment
)


from blog.forms import (
    CommentForm,
    PostForm,
    EditPostForm,
)

class BaseBlogListView(ListView):
    """Base view blog list view:

    queryset: The default queryset is ordered by the 
    newest published  

    template: /blog/blog_home.html

    context: categories with most posts
    """
    model = Post
    paginate_by = 9
    template_name = 'blog/blog_home.html'

    def get_if_parameter_in_request(self, parameter):

        return parameter in self.request.GET

    def get_content_of_parameter_in_request(self, parameter):
        if self.get_if_parameter_in_request(parameter):
            return str(self.request.GET.get(parameter))
        else:
            return None

    def get_content_of_parameter_in_request_no_assertion(self, parameter):
        return str(self.request.GET.get(parameter))

    def get_queryset(self):
        query = self.get_content_of_parameter_in_request("filter")

        if query == "liked":
            # returns the most liked posts
            return self.model.objects.annotate(
                most_liked=Count("upvotes")).order_by("-most_liked")

        elif query == "commented":
            return self.model.objects.annotate(
                most_commented=Count("comment")).order_by("-most_commented")

        # If there isn't filter, Posts are ordered by date
        return self.model.objects.all().order_by("-date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat_items"] = ALL_CATEGORIES[:5]

        return context


class BaseBlogSearchView(BaseBlogListView):
    """Extends BaseBlogListView
    Same parameters and models
    Adds search functionality

    queryset: Latest(Default), Most liked (?filter=liked), search (?q={SEARCH query})
    context: Main category items, string of ?q query

    Doesn't paginate
    """

    paginate_by = None
    context_object_name = "posts"

    def get_queryset(self):
        search_queryset = None

        search_parameter = self.get_content_of_parameter_in_request("q")
        # If q is in the request, the process continues
        # If q is in the request and it isn't empty gets the query results
        if search_parameter not in ["", " "] and search_parameter is not None:

            # Get the query from the request
            query = search_parameter

            search_queryset = self.model.objects.filter(
                Q(title__icontains=query) | Q(
                    description__icontains=query) | Q(body__icontains=query)
            ).distinct().order_by("-date")

        return search_queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["string_query"] = self.get_content_of_parameter_in_request("q")
        return context


class BaseCreateCommentView(CreateView):

    """Base Create Comment

    Extends from Create view

    Involves all the functionality of creating a commentary:
    - Success url
    - Form validation
    """

    # Creates a comment
    model = Comment
    form_class = CommentForm
    
    # Returns the detail post
    def get_detail_post(self):
        return get_object_or_404(Post, id=self.kwargs['pk'])


    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('blog:article', kwargs={'pk': self.kwargs['pk']})

    # Validates the form with the user, and post
    def form_valid(self, form):

        detail_post = self.get_detail_post()

        user = self.request.user

        form.instance.commenter = user

        form.instance.post = detail_post

        return super().form_valid(form)


class BaseArticleDetailView(BaseCreateCommentView):
    """Base Article Detail View
    Extends Base Create Comment class

    Gets all the detail article related information
    """


    def get_context_data(self, **kwargs):
        # Gets the previous info
        context = super().get_context_data(**kwargs)

        # Get the post with the self.pk
        detail_post = self.get_detail_post()

        # Pass the detail post as the object
        context["post"] = detail_post

        # Calls the Post property of counting the upvotes of the post
        context["upvotes"] = detail_post.total_likes()

        upvoted = False

        # If the post has upvotes it means it's upvoted
        if detail_post.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True

        context["upvoted"] = upvoted

        try:
            # Gets all the related comments
            context["comments"] = Comment.objects.filter(
                post=detail_post).order_by('-date_added')

        except Comment.DoesNotExist:
            context["comments"] = None

        recent = True
        other_posts = Post.objects.all().order_by('-date')[:4]

        if detail_post.category:
            # If the post has a category, related posts are from the category

            related_posts = Post.objects.filter(
                category=detail_post.category).exclude(id=self.get_detail_post().id)

            if related_posts.count() > 0:
                other_posts = related_posts
                recent = False

        context["recent"] = recent
        context["other_posts"] = other_posts

        return context

class BaseCRUDPostView:

    model = Post


class BaseCreatePostView(BaseCRUDPostView,CreateView):

    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BaseEditPostView(BaseCRUDPostView, UpdateView):

    form_class = EditPostForm


class BaseDeletePostView(BaseCRUDPostView, DeleteView):

    success_url = reverse_lazy("blog:home")


def VoteView(request, pk):
    post = Post.objects.get(id=pk)

    if post.upvotes.filter(id=request.user.id).exists():
        post.upvotes.remove(request.user)
    else:
        post.upvotes.add(request.user)
    return HttpResponseRedirect(reverse('blog:article', args=[str(pk)]))
