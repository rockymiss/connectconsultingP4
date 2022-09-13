"""Views"""

from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import generic, View
from .models import BlogPost, BlogComment
from .forms import CreateBlog, CreateTestimonial, CreateComment
from django.urls import reverse_lazy
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


class BlogDetail(View):
    """
    This class will display the blog the user selects from
    the BlogPostList.  It will also render comments the 
    user makes
    """
    
    def get(self, request, slug, *args, **kwargs):
        queryset = BlogPost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.user_comments.filter(
                                             approve=True
                                             ).order_by('comment_created')
        blog_favourite = False
        if post.blog_favourite.filter(id=self.request.user.id).exists():
            blog_favourite = True

        return render(
            request,
            "blog_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "blog_favourite": blog_favourite,
                "comment_form": CreateComment()
            },
        )


    def post(self, request, slug, *args, **kwargs):
        queryset = BlogPost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.user_comments.filter(
                                             approve=True
                                             ).order_by('comment_created')
        blog_favourite = False
        if post.blog_favourite.filter(id=self.request.user.id).exists():
            blog_favourite = True

        comment_form = CreateComment(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CreateComment()

        return render(
            request,
            "blog_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "blog_favourite": blog_favourite,
                "comment_form": CreateComment()
            },
        )


# Testimonial Views

class CreateTestimonView(CreateView):
    """
    Creates Testimonial view so that user can create 
    a testionial on the front end
    """
    template_name = 'create_testimonial.html'
    form_class = CreateTestimonial
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        """
        Validates the form and adds the new testimonial to the
        index.html page

        """
        form = form.save(commit=False)
        return super().form_valid(form)

# Admin Only View


class CreateBlogView(UserPassesTestMixin, CreateView):
    """
    Creates blog view so that admin can create a new
    blog on the front end
    """
    
    def test_func(self):
        """
        Checks if superuser
        """
        return self.request.user.is_superuser

    template_name = 'create_blog.html'
    form_class = CreateBlog
    success_url = reverse_lazy('blog')
    

    def form_valid(self, form):
        """
        Validates the form and adds the new blog to the 
        blog.html page

        """
        form = form.save(commit=False)
        form.slug = slugify(form.blog_subtitle)
        return super().form_valid(form)


class ApproveComments(UserPassesTestMixin, ListView):
    """
    Creates a view of the comments to be approved, which 
    can only be access by admin. This allows admin to 
    approve comments on the frontend
    """
    
    def test_func(self):
        """
        Checks if superuser
        """
        return self.request.user.is_superuser
        
    template_name = 'approve_comments.html'
    model = BlogComment
    queryset = BlogComment.objects.filter(
        approve=False).order_by('comment_created')
    context_object_name = 'approval'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        """
        Gets the comments for approval
        """
        context = super().get_context_data(**kwargs)
        context['comments'] = BlogComment.objects.filter(
            approve=False).order_by('comment_created')
        return context
