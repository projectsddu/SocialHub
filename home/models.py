from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.conf import settings
import datetime

from login.models import customuser


class post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_url = models.URLField(null=False)
    is_reported = models.BooleanField(default=False)
    location = models.CharField(
        max_length=30, default="Somewhere in the World")
    date_posted = models.DateField()
    caption = models.CharField(max_length=40, default="Chilling in the world!")

    def __str__(self):
        return str(self.post_id)


class comments(models.Model):
    post_id = models.ForeignKey(post, on_delete=models.CASCADE)
    commenter_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    date_added=models.DateField(default=datetime.date.today)


class likes(models.Model):
    like_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(post, on_delete=models.CASCADE)
    liker_user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_liked = models.DateField(default=datetime.date.today)

    def get_treding():
        return likes.objects.raw("select like_id,Post_id from home_likes")


class UploadImage(models.Model):
    """
    Define how the user will upload images
    """
    # link author to registered user
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    myimage = models.ImageField(upload_to='myimages/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class FriendRequest(models.Model):
    # username = models.CharField()
    sender_username = models.CharField(max_length = 100)
    receiver_username = models.CharField(max_length = 100)
    date_received = models.DateField(auto_now=True)
    request_status = models.BooleanField(default=False)
    date = models.DateField(default=datetime.date.today)
    def get_followed(self):
        return self.request_status
    

class Notifications(models.Model):
    notif_id=models.AutoField(primary_key=True)
    notif_title=models.CharField(max_length=100)
    notif_msg=models.TextField()
    notify_to=models.ForeignKey(User,on_delete=models.CASCADE)
    date_added=models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.notif_msg
    
    
