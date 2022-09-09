"""Admin Panel"""

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost, BlogComment, Testimonial


@admin.register(BlogPost)
class PostAdmin(SummernoteModelAdmin):
    """
    Applies display, filter, search, prepopulated fields
    and summernote functionality to the BlogPost Model
    on the admin panel

    """

    search_fields = ['blog_title', 'blog_content']
    list_display = ('blog_title',
                    'slug',
                    'status',
                    'blog_created_on',
                    'author')
    list_filter = ('status', 'blog_created_on')
    prepopulated_fields = {'slug': ('blog_title',)}
    summernote_fields = ('blog_content')


@admin.register(BlogComment)
class CommentAdmin(admin.ModelAdmin):
    """
    Applies display, filter, search and action functionality
    to the BlogPost Model on the admin panel
    """
    list_display = ('name',
                    'comment_created',
                    'comment_body',
                    'approve')
    list_filter = ('approve', 'comment_created')
    search_fields = ('name', 'comment_body')
    actions = ['approve_comments']

    def comment_approve(self, request, queryset):
        """
        Creates an action which allows admin to approve a comment
        """
        queryset.update(approve=True)


@admin.register(Testimonial)
class PostTestimonal(SummernoteModelAdmin):
    """
    Applies display, filter, and search functionality
    to the BlogPost Model on the admin panel
    """

    search_fields = ['company_name', 'name',]
    list_display = (
                    'name',
                    'company_name',
                    'content',
                    'approve',
                    'date_created')
    list_filter = ('date_created', 'approve',)
    summernote_fields = ('content')
    actions = ['approve_testimonials']

    def testimonial_approve(self, request, queryset):
        """
        Creates an action which allows admin to approve a comment
        """
        queryset.update(approve=True)
