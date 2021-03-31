from django.contrib import admin
from .models import comments,post,likes,FriendRequest,Notifications,user_secret_key

admin.site.register(comments)
admin.site.register(likes)
admin.site.register(FriendRequest)
admin.site.register(post)
admin.site.register(Notifications)
admin.site.register(user_secret_key)