"""
Views for Contact App
"""
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .models import ContactUs
from .forms import ContactForm


class ContactCreate(CreateView):
    """
    Creates a view so that users 
    can fill out a contact form to 
    contact the owners
    """
    model = ContactUs
    template_name = 'contactus/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy("thankyou")


class ThankYouView(TemplateView):
    """
    Creates view for Thank You Page
    """
    template_name = "contactus/thankyou.html"