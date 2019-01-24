from django.contrib import admin
from django.urls import path
from . import views
app_name = "users-api"

urlpatterns = [
    path('register/', views.UserCreateAPIView.as_view(), name='register'),
    path('login/', views.UserLoginAPIView.as_view(), name='login'),


    #url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]