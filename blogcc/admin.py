"""Admin Panel"""

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost


@admin.register(BlogPost)
class PostAdmin(SummernoteModelAdmin):
    """
    Applies display, filter, search, prepopulated fields
    and summernote functionality to the BlogPost Model
    on the admin panel

    """

    search_fields = ['blog_title', 'blog_content']
    list_display = ('blog_title', 'status', 'blog_created_on', 'author')
    list_filter = ('status', 'blog_created_on')
    prepopulated_fields = {'slug': ('blog_title',)}
    summernote_fields = ('blog_content')