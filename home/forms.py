from django import forms

class ImageFrom(forms.Form):
    Caption=forms.CharField(max_length=50, required=False)
    Image=forms.ImageField(required=False)
