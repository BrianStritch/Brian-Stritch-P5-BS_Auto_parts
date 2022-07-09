""" imports for favourites admin.py """
# imports
# 3rd party imports from django
from django.contrib import admin

# internal imports from BS_Auto_parts
from .models import Favourites


class FavouritesAdmin(admin.ModelAdmin):
    """
    Admin class for the Favourites model.
    """
    list_display = (
        'username',
        'products'
    )
    search_fields = (
        'username',
        'products'
    )
    list_filter = (
        'username',
    )
    list_per_page = 20


admin.site.register(Favourites, FavouritesAdmin)
