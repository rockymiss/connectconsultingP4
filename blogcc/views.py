"""Views"""

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from django.views import generic
from .models import BlogPost
from .forms import CreateBlog
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.text import slugify


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


class CreateBlogView(CreateView):
    """
    Creates blog view so that admin can create a new 
    blog on the front end   
    """
    template_name = 'create_blog.html'
    form_class = CreateBlog
    success_url = reverse_lazy('blogs')


    def form_valid(self, form):
        """
        Validates the form and adds the new blog to the 
        blog.html page

        """
        form = form.save(commit=False)
        messages.success(
            self.request,
            'You have added a new blog')
        form.slug = slugify(form.blog_subtitle)
        return super().form_valid(form)
