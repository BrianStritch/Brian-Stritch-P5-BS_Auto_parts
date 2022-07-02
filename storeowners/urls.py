from django.urls import path
from . import views

urlpatterns = [
    path('', views.StoreManagement.as_view(), name='store_management'),
    path('stock_management/', views.StockManagement.as_view(), name='stock_management'),
    path('contact_query/', views.QueryManagement.as_view(), name='contact_query'),
    path('update_new_user_query/<int:pk>/', views.ToggleNewUserContactUsStatus.as_view(), name='update_new_query'),
    path('update_existing_user_query/<int:pk>/', views.ToggleExistingContactUsStatus.as_view(), name='update_existing_query'),    
]