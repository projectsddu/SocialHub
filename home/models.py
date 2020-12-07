from django.db import models
from django.contrib.auth.models import User
from django import forms


class post(models.Model):
    post_id=models.AutoField(primary_key=True)
    user_fk=models.ForeignKey(User,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='home/post_images',null=False)
    is_reported=models.BooleanField(default=False)
    location=models.CharField(max_length=30,default="Somewhere in the World")
    date_posted=models.DateField()
    caption=models.CharField(max_length=40,default="Chilling in the world!")
    def __str__(self):
        return str(self.post_id)

class comments(models.Model):
    post_id=models.ForeignKey(post,on_delete=models.CASCADE)
    commenter_user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_text=models.TextField()

class likes(models.Model):
    post_id=models.ForeignKey(post,on_delete=models.CASCADE)
    liker_user=models.ForeignKey(User,on_delete=models.CASCADE)







