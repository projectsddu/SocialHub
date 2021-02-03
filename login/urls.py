from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.login,name='login'),
    path('login_user',views.login_user,name="user_in"),
    path('signup',views.signup,name="signup")
]
