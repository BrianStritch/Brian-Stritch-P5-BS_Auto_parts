from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Favourites(models.Model):
    """
    This model is for a users favourites list
    """
    class Meta:
        verbose_name_plural = 'Favourites'

    products = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_favourites')
    

    def __str__(self):       
        return f"{self.username}'s Favourites"