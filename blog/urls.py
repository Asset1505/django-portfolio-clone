"""Defines url patterns for blog."""

from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    #Blog page
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>', views.detail, name='detail_blog'),
]
