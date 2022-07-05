from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsletterSignup.as_view(), name='newsletter'),
    path('subscribers_list/', views.NewsletterSubscribers.as_view(), name='subscriber_list'),
]
