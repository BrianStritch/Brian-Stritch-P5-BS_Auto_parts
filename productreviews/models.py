"""
    imports  
"""
# third party imports
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.shortcuts import reverse
from products.models import Product


STATUS = (
    (0, 'Draft'),
    (1, 'Published')
    )


class ProductReview(models.Model):
    """
        Class based model for Reviews
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=200, unique=True)

    slug = models.SlugField(max_length=200, unique=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_review_posts')

    updated_on = models.DateTimeField(auto_now=True)

    content = models.TextField()    

    excerpt = models.TextField(blank=True)

    created_on = models.DateTimeField(auto_now_add=True)

    status = models.IntegerField(choices=STATUS, default=0)

    likes = models.ManyToManyField(User, related_name='product_review_likes', blank=True)

    class Meta:
        """
            meta class to set the order in which
            the reviews are displayed
        """
        ordering = ['-created_on']

    def get_absolute_url(self):
        """
            function to define the reverse URL
            for after a product review is created or edited
        """
        return reverse('products')  

    def save(self, *args, **kwargs):
        """
            function to edit and save the slug
            for after a review is created or edited
        """
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self): 
        """
            function to return the review title as a string
        """
        return str(self.title)

    def number_of_likes(self):
        """
            function to return the number of likes on a review
        """
        return self.likes.count()


class ProductReviewComment(models.Model):
    """
        Class based model for Comments
    """

    product_review = models.ForeignKey(
        ProductReview,
        on_delete=models.CASCADE,
        related_name='product_review_comments'
        )

    name = models.CharField(max_length=80)

    email = models.EmailField()

    body = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

    approved = models.BooleanField(default=False)

    class Meta:
        """
            meta class to set the order in which
            the reviews are displayed
        """
        ordering = ['created_on']

    def __str__(self):
        """
            function to return the commentbody and the author as a string
        """
        return f"Comment {self.body} by {self.name}"

    def get_absolute_url(self):
        """
            function to define the reverse URL
            for after a comment is created or edited
        """
        return reverse('products')   # --------------------- set reverse url --------------

