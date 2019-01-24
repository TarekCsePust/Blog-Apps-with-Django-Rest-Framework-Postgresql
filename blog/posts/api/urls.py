from django.contrib import admin
from django.urls import path
from . import views
app_name = "posts-api"
urlpatterns = [
    path('', views.PostListAPIView.as_view(), name='list'),
    path('create/', views.PostCreateAPIView.as_view(), name='create'),
    path('<slug>/', views.PostDetailAPIView.as_view(), name='detail'),
    path('<slug>/edit/', views.PostUpdateAPIView.as_view(), name='update'),
    path('<slug>/delete/',views.PostDeleteAPIView.as_view(), name='delete'),
]
