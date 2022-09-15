"""
urls for blog app
"""
from django.urls import path
from .views import ContactCreate, ThankYouView


urlpatterns = [
    path('contactus/contact', ContactCreate.as_view(), name="contact"),
    path('contactus/thankyou', ThankYouView.as_view(), name="thankyou")
]