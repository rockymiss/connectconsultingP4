"""
urls for blog app
"""
from django.urls import path
from .views import ContactCreate, ThankYouView, MessageView, DeleteMessage


urlpatterns = [
    path('contact/', ContactCreate.as_view(), name="contact"),
    path('thankyou/', ThankYouView.as_view(), name="thankyou"),
    path('getmessage/', MessageView.as_view(), name="getmessage"),
    path('contactus/message_confirm_delete/<int:pk>/',
         DeleteMessage.as_view(), name="message_confirm_delete"),
]
