from django.contrib import admin
from django.urls import path
from . import views
app_name = "posts"
urlpatterns = [
    path('',views.post_list,name="list"),
    path('create/', views.post_create,name="post_create"),
    path('<slug>/', views.post_detail,name="detail"),
    path('<slug>/edit/', views.post_update,name="update"),
    path('<slug>/delete/', views.post_delete,name="post_delete"),
]
