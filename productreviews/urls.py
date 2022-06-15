from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:pk>/', views.CreateProductReview.as_view(), name='create_product_review'),
    path('edit_review/<int:pk>/', views.EditProductReview.as_view(), name='edit_product_review'),
    path('delete_review/<int:pk>/', views.DeleteProductReview.as_view(), name='delete_product_review'),
]