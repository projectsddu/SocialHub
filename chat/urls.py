from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('/chat_home',views.home,name="chat_home"),
    path('/chat_redirect/<slug:slug>',views.chat_redirect,name="chat_redirect"),
    path('/<slug:slug>',views.index,name="index"),

]