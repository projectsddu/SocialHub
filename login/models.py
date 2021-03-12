from django.db import models
from django.contrib.auth.models import User

class customuser(models.Model):
    city_of_residence=models.CharField(max_length=40)
    country_of_residence=models.CharField(max_length=40)
    Image=models.ImageField(upload_to='home/user_images',default="media/asset/images/1_TrnL6Aj.png")
    bio=models.TextField()
    user_inher=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.CharField(max_length=150,default="not@provided.com")

