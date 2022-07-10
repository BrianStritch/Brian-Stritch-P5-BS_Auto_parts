# imports
# 3rd party imports from django
from django.urls import path

# internal imports from BS_Auto_parts
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history,
         name='order_history'),
    path('edit_profile/', views.EditProfile.as_view(), name='edit_profile'),
    path('delete_profile/<int:pk>/',
         views.DeleteProfile.as_view(),
         name='delete_profile'),
    path('register/', views.SignUp.as_view(), name='sign_up'),
]
