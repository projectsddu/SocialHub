from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name="business_dashboard"),
    path('/your_business', views.business, name="business"),
    path('/advertise', views.advertise, name="advertise"),
    path('/getdata', views.getFollowers, name="getdata"),
]
    
