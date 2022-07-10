"""
    imports  -------------Reviews forms.py----------------------
"""
# third party imports
from django import forms
# internal imports
from .models import ProductReview, ProductReviewComment


class ProductReviewCommentForm(forms.ModelForm):
    """
    Class based form to create new product review comments using the
    product review comments model
    """

    class Meta:
        """
        Class to indicate which model to use and to
        set the fields in the create comment model form
        """
        model = ProductReviewComment
        fields = ('body', )


class CreateProductReviewForm(forms.ModelForm):
    """
        Class based form to set the fields in
        the Create Product Review model form for creating a new product review
    """

    class Meta:
        """
        Class to indicate which model to use and to
        set the fields in the create review model form
        """
        model = ProductReview
        fields = ('title', 'content', 'summary')
