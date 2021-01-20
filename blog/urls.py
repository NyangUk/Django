# blog/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path(r'', views.post_list, name='post_list'),
    path(r'post/<int:pk>/', views.post_detail, name='post_detail'),
]