from django import forms
from .models import Favourites

class Favouriteform(forms.ModelForm):

    class Meta:
        model = Favourites
        fields = ('username', 'products',)