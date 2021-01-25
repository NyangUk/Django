# accounts/urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(r'signup',views.signup,name='signup' ),
    path(r'login',views.login,name='login' ),
    path(r'logout',views.logout,name ='logout' ),
]
