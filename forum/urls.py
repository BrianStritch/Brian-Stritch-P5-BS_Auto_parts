""" forum urls.py """
# imports
# 3rd party imports from django
from django.urls import path

# internal imports from BS_Auto_parts
from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('topic/<slug:slug>/', views.TopicList, name='topic_list'),
    path('post_detail/<int:pk>/', views.PostDetail, name='post_detail'),
    path('create_category/',
         views.CreateCategory.as_view(),
         name='create_category'),
    path('edit_forum_category/<int:pk>/',
         views.EditCategory.as_view(),
         name='edit_forum_category'),
    path('delete_forum_category/<int:pk>/',
         views.DeleteCategory.as_view(),
         name='delete_forum_category'),
    path('create_topic/', views.CreateTopic.as_view(), name='create_topic'),
    path('edit_forum_topic/<int:pk>/',
         views.EditTopic.as_view(),
         name='edit_forum_topic'),
    path('delete_forum_topic/<int:pk>/',
         views.DeleteTopic.as_view(),
         name='delete_forum_topic'),
    path('create_post/<int:pk>/',
         views.CreatePost.as_view(),
         name='create_post'),
    path('edit_forum_post/<int:pk>/',
         views.EditPost.as_view(),
         name='edit_forum_post'),
    path('delete_forum_post/<int:pk>/',
         views.DeletePost.as_view(),
         name='delete_forum_post'),
    path('forum_post/like/<int:pk>/',
         views.PostLike.as_view(),
         name='post_like'),
    path('create_forum_comment/<int:pk>/',
         views.CreateForumComment.as_view(),
         name='create_forum_comment'),
    path('edit_forum_comment/<int:pk>/',
         views.EditForumComment.as_view(),
         name='edit_forum_comment'),
    path('delete_forum_comment/<int:pk>/',
         views.DeleteForumComment.as_view(),
         name='delete_forum_comment'),
    path('forum_comment/like/<int:pk>/',
         views.CommentLike.as_view(),
         name='forum_comment_like'),
]
