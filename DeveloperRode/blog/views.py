from django.shortcuts import render
from django.views import View


# Create your views here.
class BlogView(View):
    def get(self, request):
        """
        Return the blog view
        """
        return render(request, 'blog/index.html')
