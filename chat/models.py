from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class Chat(models.Model):
#     chat_id=models.AutoField(primary_key=True)
#     chat_msg=models.TextField()
#     chat_time=models.DateTimeField(auto_now_add=True)
    
# class Subcriber(models.Model):
#     subcriber=models.ForeignKey(User,on_delete=models.CASCADE)
#     chat_id=models.IntegerField()


# create chat room
class ChatRoom(models.Model):
    chat_room_id = models.IntegerField(primary_key = True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)    #created by owner
    is_group = models.BooleanField(default=False)   #check status
    
    def getChatRoomId(self):
        return self.chat_room_id
    
# store messages for specific chat room
class Message(models.Model):
    chat_room_id = models.IntegerField()
    message = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    sender=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
# already exist
class Subscriber(models.Model):
    user_fk = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    chat_room_id = models.IntegerField()
    
    
