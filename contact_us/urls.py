# imports
# 3rd party imports from django
from django.urls import path

# internal imports from BS_Auto_parts
from . import views

urlpatterns = [
    path('', views.ContactUs.as_view(), name='contact_us'),    
    path('simple/', views.SimpleContactUs.as_view(), name='simple_contact_us'),
    path('existing_user/<int:pk>', views.ExistingUsersContactUs.as_view(), name='existing_user_contact_us'),
]
