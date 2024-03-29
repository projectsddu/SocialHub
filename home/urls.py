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
    path('/add_friend/',views.add_friend,name="addfriend"),
    path('/add_friend_status/',views.add_friend_status,name="change_status_fr"),
    path('/show_follwers/<slug:slug>',views.showFollowers,name="showfollowers"),
    path('/show_following/<slug:slug>',views.showFollowing,name="showfollowing"),
    path('/remove_notification',views.removeNotifications,name="remove_notification"),
    path('/settings',views.settings,name="settings"),
    path('/delete_ac',views.delete_ac,name="del_ac"),
    path('/edit_post',views.edit_post,name="edit_post"),
    path('/add_profile_image',views.add_profile_image,name="add_profile_image"),
    path('/add_background_image',views.add_backround_image,name="add_background_image"),
    path('/delete_ac_verify',views.delete_verify_ac,name="del_ac_verify"),
    
]

