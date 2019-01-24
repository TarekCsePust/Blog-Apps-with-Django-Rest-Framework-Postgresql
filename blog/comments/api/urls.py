from django.contrib import admin
from django.urls import path
from . import views
app_name = "comments-api"

urlpatterns = [
    path('',views.CommentListAPIView.as_view(), name='list'),
    path('comment/create/', views.CommentCreateAPIView.as_view(), name='create'),
    path('<pk>/', views.CommentDetailAPIView.as_view(), name='thread'),


    #url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]