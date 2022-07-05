# imports
# 3rd party imports from django
from django import forms

# internal imports from BS_Auto_parts
from .models import Favourites


class Favouriteform(forms.ModelForm):

    class Meta:
        model = Favourites
        fields = ('username', 'products',)