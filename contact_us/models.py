""" imports for contact us models"""
# imports
# 3rd party imports from django
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

STATUS = ((0, 'Pending'), (1, 'Completed'))


class SiteUsersContactDetails(models.Model):
    """
    A model for obtaining users information who wish
    to be contacted by the site owners for a specific reason.
    """
    name = models.CharField(max_length=40, null=False, blank=False)

    surname = models.CharField(max_length=40, null=False, blank=False)

    email = models.EmailField(blank=False)

    message = models.TextField(blank=True)

    status = models.IntegerField(choices=STATUS, default=0)

    created_on = models.DateTimeField(auto_now_add=True)

    phone_number = models.CharField(max_length=20, null=True, blank=True)

    street_address1 = models.CharField(max_length=80, null=True, blank=True)

    street_address2 = models.CharField(max_length=80, null=True, blank=True)

    town_or_city = models.CharField(max_length=40, null=True, blank=True)

    county = models.CharField(max_length=80, null=True, blank=True)

    country = CountryField(blank_label='Country', null=True, blank=True)

    postcode = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        """
        class to set the ordering of the list
        display of site users contact details
        """
        ordering = ['-created_on']
        verbose_name_plural = 'Site Users Contact Details'

    def __str__(self):
        return f'{self.name} {self.surname}'


class ExistingUsersContactDetails(models.Model):
    """
    A model for obtaining users information who wish
    to be contacted by the site owners for a specific reason.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    message = models.TextField(max_length=250, blank=True)

    status = models.IntegerField(choices=STATUS, default=0)

    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        class to set the ordering of the list
        display of site users contact details
        """
        ordering = ['-created_on']
        verbose_name_plural = 'Existing Users Contact Details'
