"""
Views for Contact App
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, TemplateView, ListView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
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


class MessageView(UserPassesTestMixin, ListView):
    """
    Checks to see if user is superuser, gets a list of
    Messages made by user 
    """

    def test_func(self):
        """
        Checks if superuser
        """
        return self.request.user.is_superuser

    template_name = 'contactus/getmessage.html'
    model = ContactUs
    queryset = ContactUs.objects.order_by('date_created')
    context_object_name = 'getmessage'


class DeleteMessage(UserPassesTestMixin, DeleteView):
    """
    Checks to see if user is admin and allows admin
    to delete a message sent by the user 
    """
    def test_func(self):
        """
        Checks if superuser
        """
        return self.request.user.is_superuser

    def get(self, request, pk, *args, **kwargs):
        """
        gets the object instance's id and assigns primary key
        """
        getmessage = get_object_or_404(ContactUs, pk=pk)
        context = {
            'getmessage': getmessage,
        }

        return render(
            request,
            'contactus/message_confirm_delete.html',
            context
        )

    def post(self, request, pk, *args, **kwargs):
        """
        gets the message the user made Admin can
        then delete the content
        """

        getmessage = get_object_or_404(ContactUs, pk=pk)
        getmessage.delete()

        return redirect('getmessage')

