from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name="Search"),
    path('/search_query', views.search_query, name="search_query"),
    path('/search_result', views.search_user, name="search_user")
]
