""" imports for favourites forms.py """
# imports
# 3rd party imports from django
from django import forms

# internal imports from BS_Auto_parts
from .models import Favourites


class Favouriteform(forms.ModelForm):
    """ creates a favourite form """

    class Meta:
        """ class to set the fields in the form """
        model = Favourites
        fields = ('username', 'products',)
