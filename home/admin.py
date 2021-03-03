from django.contrib import admin
from .models import comments,post,likes,FriendRequest,Notifications

admin.site.register(comments)
admin.site.register(likes)
admin.site.register(FriendRequest)
admin.site.register(post)
admin.site.register(Notifications)