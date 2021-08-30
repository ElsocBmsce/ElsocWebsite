from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

URLPattern = [
    path("", views.index, name="home"),
    
]