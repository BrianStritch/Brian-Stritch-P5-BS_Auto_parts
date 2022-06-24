from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('topic/<slug:slug>/', views.Topic_list, name='topic_list'),
    path('post_detail/<slug:slug>/', views.Post_detail, name='post_detail'),
]
