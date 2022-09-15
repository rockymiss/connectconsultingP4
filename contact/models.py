""" Models for Contact Form """
from django.db import models


class ContactUs(models.Model):
    """
    This Model will allow the user to contact
    the owner of the website
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(default='email@gmail.com')
    message = models.TextField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        messages are displayed from oldest to newest
        """
        ordering = ['date_created']

    def __str__(self):
        """
        returns string representation of the object
        """
        return f"{self.first_name} {self.last_name}"
