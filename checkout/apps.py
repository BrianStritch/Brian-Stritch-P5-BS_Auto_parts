""" imports for checkout apps.py """
# imports
# 3rd party imports from django
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ sets default configuration of checkout """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
