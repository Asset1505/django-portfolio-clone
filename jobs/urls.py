"""Defines url patterns for jobs."""

from django.urls import path

from . import views

app_name = 'jobs'
urlpatterns = [
    #Home page
    path('', views.home, name='home'),
]
