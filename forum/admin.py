""" forum admin.py """
# imports
# 3rd party imports from django
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# internal imports from BS_Auto_parts
from .models import ForumCategory, ForumPostComment, ForumPost, ForumTopics


@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    """
    Class to set the fields to be displayed in the django
    admin panel in the review fields
    """
    prepopulated_fields = {
        'slug': ('title',)
        }
    list_display = (
        'title',
        'slug',
        'status',
        'created_on',
        )
    list_filter = (
        'status',
        'created_on',
        )
    search_fields = [
        'title',
        'content',
        ]
    summernote_fields = (
        'content'
        )
    actions = [
        'approve_posts',
        ]

    def approve_posts(self, request, queryset):
        """
        class based function to update the comment status
        from the selection in the django admin view
        """
        queryset.update(status=True)


@admin.register(ForumPostComment)
class ForumPostCommentAdmin(admin.ModelAdmin):
    """
    Class to set the fields to be displayed in the django
    admin panel in the comments fields
    """
    list_filter = (
        'approved',
        'created_on'
        )
    list_display = (
        'name',
        'body',
        'post',
        'created_on',
        'approved',
        )
    search_fields = [
        'name',
        'email',
        'body',
        ]
    actions = [
        'approve_comments',
        ]

    def approve_comments(self, request, queryset):
        """
        class based function to update the comment status
        from the selection in the django admin view
        """
        queryset.update(approved=True)


@admin.register(ForumCategory)
class ForumCategoryAdmin(admin.ModelAdmin):
    """ sets the display settings for the admin panel """
    list_display = (
        'friendly_name',
        'name',
    )
    prepopulated_fields = {
        'slug': ('name',)
        }

    ordering = ('friendly_name',)


@admin.register(ForumTopics)
class ForumTopicsAdmin(admin.ModelAdmin):
    """ sets the display settings for the admin panel """

    list_display = (
        'forum_category',
        'friendly_name',
        'name',
    )
    prepopulated_fields = {
        'slug': ('name',)
        }

    ordering = ('friendly_name',)
