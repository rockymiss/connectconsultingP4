"""Views"""

from django.shortcuts import render
from django.views.generic import TemplateView


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
