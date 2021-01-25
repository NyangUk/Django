# accounts/urls.py
from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path(r'accounts/signup', ),
    path(r'accounts/login', ),
    path(r'accounts/logout', ),
]
