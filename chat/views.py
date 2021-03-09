from django.shortcuts import render,HttpResponse
from home.views import getfollowers,getfollowing
from home.models import FriendRequest,customuser
# Create your views here.
def index(request):
    return render(request,'chat/chat.html')

def home(request):
    slug=request.user.username
    followers = FriendRequest.objects.filter(
        receiver_username=request.user.username, request_status=True)
    # print(len(followers))
    friend_list = {}
    friend_list['following'] = []
    friend_list['cur_user'] = slug
    for user in followers:
        cur_user = customuser.objects.filter(
            user_inher__username=user.sender_username)[0]
        temp = {}
        temp['username'] = user.sender_username
        temp['image'] = 'http://localhost:8000'+cur_user.Image.url
        friend_list['following'].append(temp)

    followers = FriendRequest.objects.filter(sender_username=slug, request_status=True)
    # print(len(followers))
    
    friend_list['followers'] = []
    friend_list['cur_user'] = slug
    for user in followers:
        cur_user = customuser.objects.filter(
            user_inher__username=user.receiver_username)[0]
        temp = {}
        temp['username'] = user.receiver_username
        temp['image'] = 'http://localhost:8000'+cur_user.Image.url
        friend_list['followers'].append(temp)

    print(friend_list)
    return render(request,'chat/home.html',friend_list)