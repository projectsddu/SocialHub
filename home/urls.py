from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('/like/',views.add_like_to_post,name="like"),
    path('/unlike/',views.add_unlike_to_post,name="unlike"),
    path('/search/',views.search,name="search"),
    path('/comments/',views.comment,name="search")    
]

