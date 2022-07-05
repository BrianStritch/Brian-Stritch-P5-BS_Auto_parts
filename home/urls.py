# imports
# 3rd party imports from django
from django.urls import path

# internal imports from BS_Auto_parts
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.index, name='shop'),
]
