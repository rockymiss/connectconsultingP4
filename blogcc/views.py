"""Views"""

from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views import generic
from .models import BlogPost


# Template Views 

class HomePageView(TemplateView):
    """
    Creates view for Home Page
    """
    template_name = "index.html"


class About(TemplateView):
    """
    Creates view for About Page
    """
    template_name = "about.html"


#Blog Views

class BlogPostList(generic.ListView):
    """
    Creates a list of blogs using the BlogPost Model
    """
    model = BlogPost
    queryset = BlogPost.objects.filter(status=1).order_by('-blog_created_on')
    template_name = 'blog.html'
    paginate_by = 6
    context_object_name = "bloglist"
