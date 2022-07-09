""" newsletter models.py """
# imports
# 3rd party imports from django
from django.db import models

OPTIONS = ((0, 'Subscribe:'), (1, 'Un-Subscribe:'), (2, 'Delete:'))


class Newsletter(models.Model):
    """
    A model for obtaining users information who wish
    to sign up for the website newsletter.
    """

    email = models.EmailField(unique=True)

    optin = models.IntegerField(choices=OPTIONS)

    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ returns the order to be displayed in"""
        ordering = ['-created_on']
        verbose_name_plural = 'Newsletter'
