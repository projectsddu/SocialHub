from django.contrib import admin
from .models import ChatRoom,Subscriber,Message
admin.site.register(ChatRoom)
admin.site.register(Subscriber)
admin.site.register(Message)

# Register your models here.
