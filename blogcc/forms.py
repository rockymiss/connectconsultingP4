from django import forms
from .models import BlogPost, Testimonial, BlogComment


class CreateBlog(forms.ModelForm):
    """
    A Form to allow admin to create a blog 
    on their admin page
    """
    class Meta:
        model = BlogPost
        fields = ('author',
                  'blog_title',
                  'blog_subtitle',
                  'blog_content',
                  'blog_image_1',
                  'blog_image_2',
                  'status',)
        prepopulated_fields = {'slug': ('blog_title',)}


class CreateTestimonial(forms.ModelForm):
    """
    A form to allow the user or admin to create a testimonial
    """
    class Meta:
        model = Testimonial
        fields = ('name',
                  'company_name',
                  'content',)


class CreateComment(forms.ModelForm):
    """
    A form to allow a user to leave comments on a blog post
    """
    class Meta:
        model = BlogComment
        fields = ('comment_body',)