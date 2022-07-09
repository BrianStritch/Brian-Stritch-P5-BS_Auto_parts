""" newsletter forms.py """
# imports
# 3rd party imports from django
from django import forms

# internal imports from BS_Auto_parts
from .models import Newsletter


class NewsletterSignupForm(forms.ModelForm):
    """
        Class based form to set the fields in
        the newsletter signup model form where site
        users can sign up to recieve a newsletter
    """
    class Meta:
        """
        Class to indicate which model to use and to
        set the fields in the newsletter signup model form
        """
        model = Newsletter
        fields = (
            'email',
            'optin',
            )
