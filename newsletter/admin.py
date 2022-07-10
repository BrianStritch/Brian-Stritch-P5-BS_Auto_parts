""" newsletter admin.py """
# imports
# 3rd party imports from django
from django.contrib import admin

# internal imports from BS_Auto_parts
from .models import Newsletter


@admin.register(Newsletter)
class NewsletterSignupForm(admin.ModelAdmin):
    """
    Class to set the fields to be displayed in the django
    admin panel in the newsletter fields
    """

    list_display = ('email', 'created_on', 'optin')
    search_fields = ['email', 'optin']
    actions = [
        'update_status_optin',
    ]

    def update_status_optin(self, request, queryset):
        """
        class based function to update the comment status
        from the selection in the django admin view
        """
        queryset.update(checked=True)
