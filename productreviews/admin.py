from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import ProductReview, ProductReviewComment


@admin.register(ProductReview)
class ProductReviewAdmin(SummernoteModelAdmin):
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


@admin.register(ProductReviewComment)
class ProductReviewCommentsAdmin(admin.ModelAdmin):
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
        'product_review',
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

