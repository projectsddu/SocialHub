from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('/like/',views.add_like_to_post,name="like"),
    path('/unlike/',views.add_unlike_to_post,name="unlike"),
    path('/search/',views.search,name="search"),
    path('/comments/',views.comment,name="search"),
    path('/add_comment/',views.add_comment,name="add_comment"),
    path('/profile/',views.profile,name="profile_page"),
    path('/add_post/',views.add_post,name="add_post"),
    path('/logout/',views.logout_view,name="logout"),
    path('/users/<slug:slug>',views.show_users,name="users"),
    path('/add_friend/',views.add_friend,name="addfriend")  
]

