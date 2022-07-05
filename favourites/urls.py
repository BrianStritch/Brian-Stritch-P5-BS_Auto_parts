# imports
# 3rd party imports from django
from django.urls import path

# internal imports from BS_Auto_parts
from . import views


urlpatterns = [
    path('view_favourites/', views.view_favourites, name='view_favourites'),
    path('add-remove/favourites/<int:pk>/', views.ToggleFavourite.as_view(), name='toggle-favourite'),    
]