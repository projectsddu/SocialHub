from django.shortcuts import render, HttpResponse,redirect
from home.views import getfollowers, getfollowing
from home.models import FriendRequest, customuser
from chat.models import ChatRoom, Subscriber, Message
from django.contrib.auth.models import User
# Create your views here.


def index(request, slug):

    return render(request, 'chat/chat.html')


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
        cur_user = customuser.objects.filter(
            user_inher__username=user.sender_username)[0]
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
        cur_user = customuser.objects.filter(
            user_inher__username=user.receiver_username)[0]
        temp = {}
        temp['username'] = user.receiver_username
        temp['image'] = 'http://localhost:8000'+cur_user.Image.url
        friend_list['followers'].append(temp)

    print(friend_list)
    return render(request, 'chat/home.html', friend_list)
