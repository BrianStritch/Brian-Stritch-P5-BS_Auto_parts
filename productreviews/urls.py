from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:pk>/', views.CreateProductReview.as_view(), name='create_product_review'),
    path('edit_review/<int:pk>/', views.EditProductReview.as_view(), name='edit_product_review'),
    path('delete_review/<int:pk>/', views.DeleteProductReview.as_view(), name='delete_product_review'),    
    path('create_comment/<slug:slug>/', views.ReviewsComments.as_view(), name='review_comment'),
    path('edit_review_comment/<int:pk>/', views.EditComment.as_view(), name='edit_review_comment'),
    path('delete_review_comment/<int:pk>/', views.DeleteComment.as_view(), name='delete_review_comment'),
    # path('create_comment/<int:pk>/', views.ProductReviewComment.as_view(), name='review_comment22222'),
    path('reviews/like/<int:pk>/',views.ReviewLike.as_view(),name='review_like'),
]