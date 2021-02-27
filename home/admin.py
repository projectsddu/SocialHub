from django.contrib import admin
from .models import post,comments,likes, FriendRequest
# Register your models here.
admin.site.register(post)
admin.site.register(comments)
admin.site.register(likes)
admin.site.register(FriendRequest)
