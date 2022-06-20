from django.urls import path
from . import views


urlpatterns = [
    path('view_favourites/', views.view_favourites, name='view_favourites'),
    path('add-remove/favourites/<int:pk>/', views.ToggleFavourite.as_view(), name='toggle-favourite'),
    # path('remove_product_from_favourites/<item_id>/<redirect_from>/',
    #      views.remove_product_from_favourites,
    #      name='remove_product_from_favourites'),
]