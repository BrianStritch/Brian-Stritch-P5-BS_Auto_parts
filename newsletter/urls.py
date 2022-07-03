from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsletterSignup.as_view(), name='newsletter'),
]
