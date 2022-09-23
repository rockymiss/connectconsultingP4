# pylint: disable=locally-disabled, no-member
"""Views"""

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic, View
from django.urls import reverse_lazy
from django.utils.text import slugify
from .models import BlogPost, BlogComment, Testimonial
from .forms import CreateBlog, CreateTestimonial, CreateComment

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


# Blog Views

class BlogPostList(generic.ListView):
    """
    Creates a list of blogs with status of posted
    using the BlogPost Model
    """
    model = BlogPost
    queryset = BlogPost.objects.filter(status=1).order_by('-blog_created_on')
    template_name = 'blog/blog.html'
    paginate_by = 3
    context_object_name = "bloglist"


class BlogPostDraft(LoginRequiredMixin, generic.ListView):
    """
    Creates a list of blogs with status of draft
    using the BlogPost Model
    """
    def test_func(self):
        """
        Checks if superuser
        """
        return self.request.user.is_superuser

    model = BlogPost
    queryset = BlogPost.objects.filter(status=0).order_by('-blog_created_on')
    template_name = 'blog/blog_draft.html'
    paginate_by = 3
    context_object_name = "blogdraft"


class BlogDetail(View):
    """
    This class will display the blog the user selects from
    the BlogPostList.  It will also render comments the
    user makes
    """

    def get(self, request, slug, *args, **kwargs):
        """
        Sets favourites to False and returns the blog
        in a detailed view
        """
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
            "blog/blog_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "blog_favourite": blog_favourite,
                "comment_form": CreateComment()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Takes the BlogPost Object and allows the user
        to click on an icon to mark it as a favourite
        and to leave a comment for approval underneath
        the blog.  Validates the comment and saves it for
        approval.

        """
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
            "blog/blog_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "blog_favourite": blog_favourite,
                "comment_form": CreateComment()
            },
        )


# Testimonial Views

class TestimonList(generic.ListView):
    """
    Creates a list of testimonials using the Testimonial Model
    """
    model = Testimonial
    queryset = Testimonial.objects.filter(
        approve=True).order_by('-date_created')
    template_name = 'testimonial.html'
    paginate_by = 3
    context_object_name = "testlist"


class CreateTestimonView(LoginRequiredMixin, CreateView):
    """
    Allows a user or admin to create
    a testionial on the front end
    """
    template_name = 'create_testimonial.html'
    form_class = CreateTestimonial

    def test_func(self):
        """
        Checks if user
        """
        return self.request.user.is_authenticated

    def get_success_url(self):
        """
        sets the reverse url when user
        or admin creates a new Testimonial
        """
        return reverse('create_testimonial')

    def form_valid(self, form):
        """
        Validates the form and adds the new testimonial to the
        index.html page
        """
        form = form.save(commit=False)
        messages.success(
            self.request,
            'You have added a new Testimonial and\
             it has been sent to admin for approval!')
        return super().form_valid(form)


# Favourites Post


class Favourites(View):
    """
    Creates a view so user can like blogs
    """

    def post(self, request, slug):
        """
        checks if user has id and can add or remove likes
        reloads blog_detail page
        """
        post = get_object_or_404(BlogPost, slug=slug)

        if post.blog_favourite.filter(id=request.user.id).exists():
            post.blog_favourite.remove(request.user)
        else:
            post.blog_favourite.add(request.user)

        return HttpResponseRedirect(reverse('blog_detail', args=[slug]))

# Admin Only Views


class CreateBlogView(LoginRequiredMixin, CreateView):
    """
    Creates blog view so that admin can create a new
    blog on the front end
    """

    template_name = 'blog/create_blog.html'
    form_class = CreateBlog

    def get_success_url(self):
        """
        sets the reverse url when
        admin creates a new blog
        """
        return reverse('blog')

    def test_func(self):
        """
        Checks if superuser
        """
        return self.request.user.is_superuser

    def form_valid(self, form):
        """
        Validates the form and adds the new blog to the
        blog.html page
        """

        form = form.save(commit=False)
        form.slug = slugify(form.blog_title)
        messages.success(
            self.request,
            'You have created a new Blog.  If set to posted\
                you can view the blog below, otherwise click\
                    draft blogs.')
        return super().form_valid(form)


class BlogUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Admin who is logged in can edit any blogs
    that they have created
    """
    form = CreateBlogView
    fields = ['blog_title',
              'blog_subtitle',
              'blog_content',
              'blog_image_1',
              'blog_image_2',
              'status']
    queryset = BlogPost.objects.filter(
        status=1).order_by('blog_title')

    template_name = 'blog/blog_review.html'
    success_url = reverse_lazy('blog')
    success_message = "Your blog has been updated"

    def test_func(self):
        """
        Checks if superuser
        """
        return self.request.user.is_superuser


class BlogDelete(LoginRequiredMixin, DeleteView):
    """
    Admin who is logged in can delete any blogs
    that they have created
    """
    def test_func(self):
        """
        Checks if superuser
        """
        return self.request.user.is_superuser

    model = BlogPost
    context_object_name = "bloglist"
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blog')
    success_message = "Your blog has been deleted"


class ReviewComments(LoginRequiredMixin, ListView):
    """
    Checks to see if user is superuser, gets a list of
    Comments made on a blog by user which allows Admin
    to approve Comments
    """

    def test_func(self):
        """
        Checks if superuser
        """
        return self.request.user.is_superuser

    template_name = 'review_comments.html'
    model = BlogComment
    queryset = BlogComment.objects.filter(
        approve=False).order_by('comment_created')
    context_object_name = 'to_approve'

    def get_context_data(self, **kwargs):
        """
        Gets the comments to approve
        """
        context = super().get_context_data(**kwargs)
        context[
                'comments'] = BlogComment.objects.filter(
                    approve=False).order_by('-comment_created')
        return context


class ApproveComment(LoginRequiredMixin, View):
    """
    Admin who is logged in can edit and approve comments
    that a user has created.
    """

    def test_func(self):
        """
        Checks if user is a superuser
        """
        return self.request.user.is_superuser

    def get(self, request, pk, *args, **kwargs):
        """
        gets the object instance's comment and assigns primary key
        """
        comment = get_object_or_404(BlogComment, pk=pk)
        context = {
            'comment': comment,
        }

        return render(
            request,
            'approve_comment.html',
            context
        )

    def post(self, request, pk, *args, **kwargs):
        """
        gets the comment the user made and checks
        if the comment has been approved.  Admin can
        then approve the comment
        """

        comment = get_object_or_404(BlogComment, pk=pk)
        if request.method == "POST":
            comment.approve = True
            comment.save()
        messages.success(
            self.request,
            'The comment has been posted to the blog')
        return redirect('review_comments')


class DeleteComment(LoginRequiredMixin, DeleteView):
    """
    Checks to see if user is admin and allows admin
    to delete a comment made by the user
    """
    def test_func(self):
        """
        Checks if superuser
        """
        return self.request.user.is_superuser

    def get(self, request, pk, *args, **kwargs):
        """
        gets the object instance's comment and assigns primary key
        """
        comment = get_object_or_404(BlogComment, pk=pk)
        context = {
            'comment': comment,
        }

        return render(
            request,
            'delete_comment.html',
            context
        )

    def post(self, request, pk, *args, **kwargs):
        """
        gets the comment the user made and checks
        if the comment has been approved.  Admin can
        then delete the comment
        """

        comment = get_object_or_404(BlogComment, pk=pk)
        comment.delete()
        messages.success(
            self.request,
            'The comment has been deleted')
        return redirect('review_comments')


class ReviewTestimonials(LoginRequiredMixin, ListView):
    """
    Checks to see if user is superuser, gets a list of
    Comments made on a blog by user which allows Admin
    to approve Comments
    """

    def test_func(self):
        """
        Checks if superuser
        """
        return self.request.user.is_superuser

    template_name = 'review_testimonial.html'
    model = Testimonial
    queryset = Testimonial.objects.filter(
        approve=False).order_by('-date_created')
    context_object_name = 'test_approve'

    def get_context_data(self, **kwargs):
        """
        Gets the testimonials to approve
        """
        context = super().get_context_data(**kwargs)
        context[
                'testimonials'] = Testimonial.objects.filter(
                    approve=False).order_by('-date_created')
        return context


class ApproveTestimon(LoginRequiredMixin, View):
    """
    Admin who is logged in can  approve testimonials
    that a user has created.
    """

    def test_func(self):
        """
        Checks if user is a superuser
        """
        return self.request.user.is_superuser

    def get(self, request, pk, *args, **kwargs):
        """
        gets the object instance's comment and assigns primary key
        """
        testimonial = get_object_or_404(Testimonial, pk=pk)
        context = {
            'testimonial': testimonial,
        }

        return render(
            request,
            'approve_testimonial.html',
            context
        )

    def post(self, request, pk, *args, **kwargs):
        """
        gets the content the user made and checks
        if the content has been approved.  Admin can
        then approve
        """

        testimonial = get_object_or_404(Testimonial, pk=pk)
        if request.method == "POST":
            testimonial.approve = True
            testimonial.save()
        messages.success(
            self.request,
            'The Testimonial has been posted to the blog')
        return redirect('review_testimonial')


class DeleteTestimonial(LoginRequiredMixin, DeleteView):
    """
    Checks to see if user is admin and allows admin
    to delete a testimonial made by the user
    """
    def test_func(self):
        """
        Checks if superuser
        """
        return self.request.user.is_superuser

    def get(self, request, pk, *args, **kwargs):
        """
        gets the object instance's comment and assigns primary key
        """
        testimonial = get_object_or_404(Testimonial, pk=pk)
        context = {
            'testimonial': testimonial,
        }

        return render(
            request,
            'delete_testimonial.html',
            context
        )

    def post(self, request, pk, *args, **kwargs):
        """
        gets the content the user made and checks
        if the content has been approved.  Admin can
        then delete the content
        """

        testimonial = get_object_or_404(Testimonial, pk=pk)
        testimonial.delete()
        messages.success(
            self.request,
            'The comment has been deleted')
        return redirect('review_testimonial')
