from django.db import models

OPTIONS = ((0, 'Optin'),(1, 'Optout'),(2, 'Delete:')) 

class Newsletter(models.Model):
    """
    A model for obtaining users information who wish
    to sign up for the website newsletter.
    """

    email = models.EmailField(unique=True)

    optin = models.IntegerField(choices=OPTIONS)
    
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = 'Newsletter' 
