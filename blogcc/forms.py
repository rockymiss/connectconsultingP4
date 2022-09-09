from django import forms
from .models import BlogPost


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