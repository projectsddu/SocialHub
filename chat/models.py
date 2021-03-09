from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Chat(models.Model):
    chat_id=models.AutoField(primary_key=True)
    chat_msg=models.TextField()
    chat_time=models.DateTimeField(auto_now_add=True)
    
class Subcriber(models.Model):
    subcriber=models.ForeignKey(User,on_delete=models.CASCADE)
    chat_id=models.IntegerField()
