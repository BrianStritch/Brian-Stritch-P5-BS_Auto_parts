from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateProductReview.as_view(), name='add_product'),
    path('edit/<int:productreview_id>/', views.EditProductReview.as_view(), name='edit_product_review'),
    path('delete/<int:productreview_id>/', views.DeleteProductReview.as_view(), name='delete_product_review'),
]