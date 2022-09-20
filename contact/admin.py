from django.contrib import admin
from contact.models import ContactUs

# Register your models here.


@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    """
    Applies display, filter, search and action functionality
    to the BlogPost Model on the admin panel
    """
    list_display = ('first_name',
                    'last_name',
                    'email',
                    'message',
                    'date_created')
    list_filter = ('email', 'date_created')
    search_fields = ('email', 'message')
