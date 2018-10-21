
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from .views import (
    comment_thread,
    comment_delete

    )
app_name = "comments"
urlpatterns = [
    path('<id>/',comment_thread, name='thread'),
    path('<id>/delete/', comment_delete,name='delete'),
]



