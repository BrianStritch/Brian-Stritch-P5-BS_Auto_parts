""" newsletter urls.py """
# imports
# 3rd party imports from django
from django.urls import path

# internal imports from BS_Auto_parts
from . import views

urlpatterns = [
    path('', views.NewsletterSignup.as_view(), name='newsletter'),
    path('subscribers_list/',
         views.NewsletterSubscribers.as_view(),
         name='subscriber_list'),
]
