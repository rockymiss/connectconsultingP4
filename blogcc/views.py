"""Views"""

from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HomePageView(TemplateView):
    """
    Creates view for Home Page
    """
    template_name = "index.html"
