from django.shortcuts import render,HttpResponse
from home.views import getfollowers,getfollowing
from home.models import FriendRequest,customuser
from chat.models import ChatRoom,Subscriber,Message
from django.contrib.auth.models import User
# Create your views here.
def index(request,slug):

    return render(request,'chat/chat.html')

def getChatRoom(q1,q2):
    

def chat_redirect(request,slug):
    # print(slug.split("_"))
    users = slug.split("_")
    user1 = User.objects.filter(username=users[0])[0]   # before underscore
    user2 = User.objects.filter(username=users[1])[0]   # before underscore
    # print(user1) 
    # print(user2)
    subs_of_1 = Subscriber.objects.filter(user_id = user1)
    subs_of_2 = Subscriber.objects.filter(user_id = user2)
    
    # answer = subs_of_1.values("chat_room_id") & subs_of_2.values("chat_room_id")
    # print(answer)
    
    # ans = (subs_of_1.union(subs_of_2)).difference((subs_of_1.difference(subs_of_2)).union(subs_of_2.difference(subs_of_1)))
    # print(ans)
    
    # query1 = "SELECT * FROM chat_Subscriber WHERE user_id_id = '" + str(user2) + "'"
    # # query2 = "SELECT * FROM chat_Subscriber WHERE user_id_id = '" + user2.username + "'"
    # # final_query = query1 + " INTERSECT " + query2
    # # res = Subscriber.objects.raw(final_query)
    # res = Subscriber.objects.raw(query1)
    # print(len(res))
    # print(res)
    
    # for i in res:
    #     print(i.chat_room_id)
    answer = subs_of_1 & subs_of_2
    print(answer)  
    # chat room exist
    
    
    # not exist create 
    
    return HttpResponse("<h1>Redirect</h1>")


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