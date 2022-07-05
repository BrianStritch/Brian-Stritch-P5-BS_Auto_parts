from django.urls import path
from . import views

urlpatterns = [
    path('', views.StoreManagement.as_view(), name='store_management'),
    path('stock_management/', views.StockManagement.as_view(), name='stock_management'),
    path('contact_query/', views.QueryManagement.as_view(), name='contact_query'),
    path('new_user_query/<int:pk>/', views.NewQueryDetails.as_view(), name='new_user_message'),
    path('existing_user_query/<int:pk>/', views.ExistingQueryDetails.as_view(), name='existing_user_message'),
    path('update_new_user_query/<int:pk>/', views.ToggleNewUserContactUsStatus.as_view(), name='update_new_query'),
    path('update_existing_user_query/<int:pk>/', views.ToggleExistingContactUsStatus.as_view(), name='update_existing_query'),
    path('Manufactuer_and_categories/', views.ManAndCatList.as_view(), name='man_and_cat_list'),
    path('add_manufacturer/', views.add_manufacturer, name='add_manufacturer'),
    path('edit_manufacturer/<int:pk>/', views.edit_manufacturer, name='edit_manufacturer'),
    path('delete_manufacturer/<int:pk>/', views.DeleteManufacturer.as_view(), name='delete_manufacturer'),   
    path('add_category/', views.add_category, name='add_category'),
    path('edit_category/<int:pk>/', views.edit_category, name='edit_category'),
    path('delete_category/<int:pk>/', views.DeleteCategory.as_view(), name='delete_category'),    
]