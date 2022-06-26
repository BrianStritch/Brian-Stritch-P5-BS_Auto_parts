from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('topic/<slug:slug>/', views.Topic_list, name='topic_list'),
    path('post_detail/<slug:slug>/', views.PostDetail, name='post_detail'),
    path('create_category/', views.CreateCategory.as_view(), name='create_category'),
    path('edit_forum_category/<int:pk>/', views.EditCategory.as_view(), name='edit_forum_category'),
    path('delete_forum_category/<int:pk>/', views.DeleteCategory.as_view(), name='delete_forum_category'),
    path('create_topic/', views.CreateTopic.as_view(), name='create_topic'),
    path('edit_forum_topic/<int:pk>/', views.EditTopic.as_view(), name='edit_forum_topic'),
    path('delete_forum_topic/<int:pk>/', views.DeleteTopic.as_view(), name='delete_forum_topic'),
    path('create_post/<int:pk>/', views.CreatePost.as_view(), name='create_post'),
    path('edit_forum_post/<int:pk>/', views.EditPost.as_view(), name='edit_forum_post'),
    path('delete_forum_post/<int:pk>/', views.DeletePost.as_view(), name='delete_forum_post'),
]
