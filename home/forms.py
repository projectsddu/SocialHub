from django import forms
from .models import UploadImage

class ImageFrom(forms.Form):
    Caption=forms.CharField(max_length=30)
    Location=forms.CharField(max_length=100,required=False)
    Image=forms.ImageField(required=False)
    

