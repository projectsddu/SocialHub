from django.shortcuts import render,HttpResponse
from home.models import post

def view_post(request,slug):

    return HttpResponse("<h1>Jenil</h1>")