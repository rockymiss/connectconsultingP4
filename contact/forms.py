"""Forms for Contact"""

from django.forms import ModelForm
from django.forms import Textarea
from .models import ContactUs


class ContactForm(ModelForm):
    """
    Form for user to contact owner
    """
    class Meta:
        model = ContactUs
        fields = [
            'first_name',
            'last_name',
            'email',
            'message'
        ]
        widgets = {
            'message': Textarea(
                attrs={
                    "placeholder": "Would love to hear from you"
                }
            )
        }
