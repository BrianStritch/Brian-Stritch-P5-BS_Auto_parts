from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import SiteUsersContactDetails, ExistingUsersContactDetails


@admin.register(SiteUsersContactDetails)
class SiteUsersContactDetailsAdmin(admin.ModelAdmin):
    """
    Class to set the fields to be displayed in the django
    admin panel in the review fields
    """
    
    list_display = (
        'name',
        'surname',
        'email',
        'created_on',
        )
   
    search_fields = [
        'name',
        'surname',
        ]
    summernote_fields = (
        'message'
        )


@admin.register(ExistingUsersContactDetails)
class ExistingUsersContactDetailsAdmin(admin.ModelAdmin):
    """
    Class to set the fields to be displayed in the django
    admin panel in the comments fields
    """
    
    list_display = (
        'user',
        'created_on'
        )
    search_fields = [
        'user',
        ]
    summernote_fields = (
        'message'
        )

