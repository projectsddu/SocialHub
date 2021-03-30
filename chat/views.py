from django.shortcuts import render, HttpResponse,redirect,Http404
from home.views import getfollowers, getfollowing
from home.models import FriendRequest, customuser
from chat.models import ChatRoom, Subscriber, Message
from django.contrib.auth.models import User
from login.models import customuser
# Create your views here.

def getMessagesByChatRoom(room_id,user):
    messages=Message.objects.filter(chat_room_id=room_id)
    ret_dict={}
    ret_dict["messages"]=[]
    for message in messages:
        temp_dict={}
        if user==message.sender:
            temp_dict["type"]="me"
        else:
            temp_dict["type"]="you"

        temp_dict["date"]=message.date_time
        temp_dict["sender"]=message.sender.username
        temp_dict["message"]=message.message
        ret_dict["messages"].append(temp_dict)
    return ret_dict

def getAllSubscribersByChatRoom(room_id):
    subs=Subscriber.objects.filter(chat_room_id=room_id)
    ret_list=[]
    for sub in subs:
        ret_list.append(sub.user_fk)
    return ret_list

def getSubscribersByChatRoom(room_id,cur_user):
    subs=Subscriber.objects.filter(chat_room_id=room_id)
    for sub in subs:
        if sub.user_fk!=cur_user :
            # ret_dict={}
            # ret_dict["username"]=sub.user_fk.username
            cust_user=customuser.objects.filter(user_inher=cur_user)[0]
            # ret_dict["image"]=cust_user.Image.url
            return sub.user_fk.username,cust_user.Image.url

def index(request, slug):
    ret_dict=getMessagesByChatRoom(slug,request.user)
    ret_dict["chatter"],ret_dict["chatter_image"]=getSubscribersByChatRoom(slug,request.user)
    user_obj = User.objects.filter(username=ret_dict["chatter"])[0]
    cust_user = customuser.objects.filter(user_inher=user_obj)[0]
    ret_dict["chatter_image"]=cust_user.Image.url
    print(ret_dict)
    if request.user not in getAllSubscribersByChatRoom(slug) :
        return HttpResponse("<h1>Sorry the page you requested does not exists</h1><br><h2>You are not authorized to go here</h2>")
    return render(request, 'chat/chat.html',ret_dict)


def getPrivateChatRoom(user1, user2):
    subs_of_1 = Subscriber.objects.filter(user_fk=user1)
    subs_of_2 = Subscriber.objects.filter(user_fk=user2)
    final_room = []
    for i in subs_of_1:
        for j in subs_of_2:
            if i.chat_room_id == j.chat_room_id:
                final_room.append(i.chat_room_id)
    #  This logic needs to be changed for generic groups
    print(final_room)
    if len(final_room)==0:
        print("in if")
        chat_id=len(ChatRoom.objects.all())
        new_chat_room=ChatRoom(owner=user1,chat_room_id=chat_id+1)
        new_chat_room.save()
        # room_id=new_chat_room.getChatRoomId()
        # print(room_id)
        subs_obj1=Subscriber(user_fk=user1,chat_room_id=chat_id+1)
        subs_obj2=Subscriber(user_fk=user2,chat_room_id=chat_id+1)
        subs_obj1.save()
        subs_obj2.save()
        print(subs_obj1,subs_obj2)
        
        
        final_room.append(chat_id+1)
        print(final_room)
    return final_room[0]


def chat_redirect(request, slug):
    users = slug.split("_")
    user1 = User.objects.filter(username=users[0])[0]   # before underscore
    user2 = User.objects.filter(username=users[1])[0]   # before underscore
    print(getPrivateChatRoom(user1, user2))
    return redirect("http://localhost:8000/chat/"+str(getPrivateChatRoom(user1,user2)))


# Rendering home page
def home(request):
    slug = request.user.username
    followers = FriendRequest.objects.filter(
        receiver_username=request.user.username, request_status=True)
    # print(len(followers))
    friend_list = {}
    friend_list['following'] = []
    friend_list['cur_user'] = slug
    for user in followers:
        cur_user = customuser.objects.filter(user_inher__username=user.sender_username)
        cur_user=cur_user[0]
        print(cur_user)
        temp = {}
        temp['username'] = user.sender_username
        temp['image'] = 'http://localhost:8000'+cur_user.Image.url
        friend_list['following'].append(temp)

    followers = FriendRequest.objects.filter(
        sender_username=slug, request_status=True)
    # print(len(followers))

    friend_list['followers'] = []
    friend_list['cur_user'] = slug
    for user in followers:
        print(followers)
        cur_user = customuser.objects.filter(
            user_inher__username=user.receiver_username)[0]
        temp = {}
        temp['username'] = user.receiver_username
        temp['image'] = 'http://localhost:8000'+cur_user.Image.url
        if temp not in friend_list["following"]:
            friend_list['followers'].append(temp)
    # friend_list["followers"]=set(friend_list["followers"])
    print(friend_list)
    return render(request, 'chat/home.html', friend_list)
