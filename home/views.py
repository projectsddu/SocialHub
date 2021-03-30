import os
from django.conf import settings as settings
import random
from .models import post, likes
from login.models import customuser
from .forms import ImageFrom,UserProfilImage
from .models import UploadImage, post, FriendRequest,Notifications,comments,user_secret_key
from datetime import datetime,date
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import operator
from login.views import sending_mail

def getPostByUser(user_obj):
    posts=post.objects.filter(user_fk=user_obj).order_by("date_posted").reverse()
    return posts


def getPostByFollowings(current_user):
    
    followings = getfollowing(current_user,True)
    cur_user = User.objects.filter(username = current_user)[0]
    # print(cur_user)
    post_list = []
    own_post = post.objects.filter(user_fk = cur_user, date_posted = date.today())
    
    # print(own_post)
    for f in followings:
        username = User.objects.filter(username = f.receiver_username)[0]
        posts = post.objects.filter(user_fk = username)
        for p in posts:
            post_list.append(p)
            
    post_list.sort(reverse = True)
    if len(own_post) != 0:
        own_post = own_post[0]
        post_list.insert(0,own_post)
    return post_list
    

def add_notification(notif_title,notif_msg,notify_to):
    notification = Notifications(notif_title = notif_title, notif_msg = notif_msg, notify_to = notify_to)
    notification.save()

def getfollowers(username,full=False):
    query = FriendRequest.objects.filter(
        receiver_username=username, request_status=True)
    if full==False:
        return len(query)
    else:
        return query

def getfollowing(username,full=False):
    query = FriendRequest.objects.filter(
        sender_username=username, request_status=True)
    if full==False:
        return len(query)
    else:
        return query

def getRequests(cur_user_name):
    unm = cur_user_name.get_username()
    reqs = FriendRequest.objects.filter(
        receiver_username=unm, request_status=False).order_by('date').reverse()
    req_list = []
    for req in reqs:
        req_dict = {}
        req_dict['sender_name'] = req.sender_username
        req_list.append(req_dict)
    return req_list


def getLikesByPost(post_obj, cur_user,option=False):

    like = likes.objects.filter(post_id=post_obj.post_id)
    like_count = len(like)
    if option==True:
        return like_count
    you = likes.objects.filter(post_id=post_obj.post_id, liker_user=cur_user)
    if len(you) == 1:
        return "You and "+str(like_count-1)+" other"
    return str(like_count)+" people"


def get_notifs(user):
    query=Notifications.objects.filter(notify_to=user).order_by('date_added').reverse()
    notification=[]
    for cur_query in query:
        cur_dict={}
        cur_dict['message']=cur_query.notif_msg
        cur_dict['date']=cur_query.date_added
        cur_dict["id"]=cur_query.notif_id
        cur_dict["title"]=cur_query.notif_title
        notification.append(cur_dict)
    return notification

def getCommentsByPosts(pid,getall=False):
    comments_list=[]
    comment_objs=comments.objects.filter(post_id=pid).order_by('date_added').reverse()
    a=0
    for comment in comment_objs:
        if a==3 and getall == False:
           break
        else:
            a=a+1
        dict_temp={}
        commentor=comment.commenter_user.username
        comment_msg=comment.comment_text
        dict_temp['commentor']=commentor
        dict_temp['msg']=comment_msg
        comments_list.append(dict_temp)
    return comments_list



@login_required
def index(request):
    user_name = request.user
    print(user_name.username)
    posts_to_show = []
    posts_query = getPostByFollowings(user_name)
    print(posts_query)
    print("++++++++++++++++++++++++++++++++++++++++")
    print(getRequests(request.user))
    reqs = getRequests(request.user)
    print("++++++++++++++++++++++++++++++++++++++++")
    for i in posts_query:
        owner = i.user_fk.username
        location = i.location
        caption = i.caption
        date_posted = i.date_posted
        likedby = getLikesByPost(i, request.user)
        image_url = i.photo_url
        current_user = i.user_fk
        current_user_profile = customuser.objects.filter(
            user_inher=current_user)
        user_image_url = "http://localhost:8000"+current_user_profile[0].Image.url
        user_background_image_url = "http://localhost:8000/media/"+current_user_profile[0].Image_background.url
        # just send 3-4 comments over here and then make another app for viewing whole full page posts
        comments = [{'name': 'jenil', 'comment': 'Wow when did you go here'}, {
            'name': 'Kenil', 'comment': 'Take us also'}]
        quer = likes.objects.filter(post_id=i.post_id, liker_user=user_name)
        final_bool = False
        if len(quer) == 0:
            final_bool = False
        else:
            final_bool = True
        print(current_user_profile)
        posts_to_show.append({'owner': owner, 'location': location, 'caption': caption, 'date': date_posted, 'likedby': likedby,
                              'image_url': image_url,'user_background_image':user_background_image_url, 'post_id': i.post_id, 'poster_image_url': user_image_url, 'comments': getCommentsByPosts(i), 'isliked': final_bool})
        print(caption)

    user_details_dict = {
        'name': str(user_name.username),
        'posts': posts_to_show,
        'notif': get_notifs(request.user),
        'pendings': reqs,

    }
    return render(request, 'home/home.html', user_details_dict)


@csrf_exempt
def add_like_to_post(request):
    if request.method == 'POST':
        print(request.POST)
        pid = request.POST['post_liked']
        liker = request.POST['liker_name']
         
        post_given = post.objects.filter(post_id=pid)[0]
        owner = post_given.user_fk
        print(owner)
        # print(type(post_given[0]))
        liker = User.objects.filter(username=liker)[0]
        like_given = likes(post_id=post_given, liker_user=liker)
        like_given.save()
        notification = Notifications(notif_title=liker.username +" Liked your post.",notify_to=owner)
        # notification.save()
        add_notification(liker.username +" Liked your post.","",owner)
        return HttpResponse("recieved post")
    else:
        return HttpResponse("<h1>404 Page not found</h1>")


@csrf_exempt
def add_unlike_to_post(request):

    # just check the unliker name as in reponsive we were getting \n\n jenil \n\n just remove \n
    if request.method == 'POST':
        print(request.POST)
        pid = request.POST['post_unliked']
        unliker = request.POST['unliker_name']
        unliker = User.objects.filter(username=unliker)[0]
        post_given = post.objects.filter(post_id=pid)[0]
        remove_like = likes.objects.filter(
            liker_user=unliker, post_id=post_given)[0]
        remove_like.delete()
        print("post unliked")
        return HttpResponse("recieved post")
    else:
        return HttpResponse("<h1>404 Page not found</h1>")


@csrf_exempt
def comment(request):
    json_data = {'comments': [
        {'name': 'user_1', 'comment': 'jenil is a boy'},
        {'name': 'user_1', 'comment': 'jenil is a boy'},
        {'name': 'user_1', 'comment': 'jenil is a boy'},
        {'name': 'user_1', 'comment': 'jenil is a boy'},

    ]}
    print(request.POST)
    return JsonResponse(json_data)


def search(request):
    # let us consider that the search user
    json_data = {
        'users': [
            {
                'name': 'Jenik Vekariya',
                'photo': 'https://source.unsplash.com/1600x900/?nature,mountain',
                'occupation': 'SDE at Google'
            },
            {
                'name': 'Harshvardhan Sharma',
                'photo': 'https://source.unsplash.com/1600x900/?nature,water',
                'occupation': 'SDE at Amazon'
            }
        ]
    }
    return JsonResponse(json_data)


@csrf_exempt
def add_comment(request):
    if request.method == 'GET':
        return HttpResponse("<h1>404 Page Not Found</h1>")
    else:

        post_fetched = post.objects.filter(post_id=request.POST['post_id'])[0]
        owner = post_fetched.user_fk.username
        commentor = request.POST['comentr']
        filter_user = User.objects.filter(username=commentor)[0]
        print(type(filter_user))
        # function call
        add_notification(commentor + " commented on your post.","",post_fetched.user_fk)
        # print(owner)
        # print(request.POST['comment'])
        # print(request.POST['comentr'])
        comment_ob=comments(commenter_user=filter_user,post_id=post_fetched,comment_text=request.POST['comment'])
       
        print(comment_ob)
        comment_ob.save()
        return HttpResponse("comment added")

# Renders current user's profile


def profile(request):
    # name=request.
    prof_user = customuser.objects.filter(user_inher=request.user)[0]
    print(prof_user.bio)
    users_dict = {'bio': prof_user.bio, 'followed': True}
    posts = post.objects.filter(
        user_fk=request.user).order_by("post_id").reverse()
    # posts=sorted(posts,key=operator.attrgetter('date_posted'))
    no_of_posts = len(posts)
    users_dict['n_posts'] = no_of_posts
    users_dict['following'] = getfollowing(prof_user.user_inher.username)
    users_dict['followers'] = getfollowers(prof_user.user_inher.username)
    users_dict['user_image'] = "http://localhost:8000"+prof_user.Image.url
    users_dict['user_background_image'] = "http://localhost:8000"+prof_user.Image_background.url
    users_dict['posts'] = []
    for post1 in posts:
        user_post_obj = {}
        user_post_obj['photo_url'] = "http://localhost:8000/media/" + \
            post1.photo_url
        user_post_obj['post_id'] = post1.post_id
        user_post_obj['likes'] = len(
            likes.objects.filter(post_id=post1.post_id))
        # Add here one for comment
        user_post_obj['comments'] = 30
        users_dict['posts'].append(user_post_obj)
    print(users_dict)
    return render(request, 'home/profile_base.html', users_dict)


def show_users(request, slug):
    print(slug)
    req_username = request.user.username
    var = User.objects.filter(username=slug)
    print(type(req_username))
    print(var[0])
    prof_user = customuser.objects.filter(user_inher=var[0])[0]
    # print(prof_user.bio)
    user_dict = {'bio': prof_user.bio, 'followd': True}
    allowed = False
    allowed_obj_1 = FriendRequest.objects.filter(sender_username = req_username, receiver_username = slug, request_status = True)
    allowed_obj_2 = FriendRequest.objects.filter(sender_username = slug, receiver_username = req_username, request_status = True)
    
    print(allowed_obj_1, allowed_obj_2)
    if len(allowed_obj_1) != 0 or len(allowed_obj_2) != 0:
        allowed = True
    
    posts = post.objects.filter(user_fk=var[0]).order_by("post_id").reverse()
    no_of_posts = len(posts)
    user_dict['n_posts'] = no_of_posts
    user_dict['following'] = getfollowing(prof_user.user_inher.username)
    user_dict['followers'] = getfollowers(prof_user.user_inher.username)
    user_dict['user_image'] = "http://localhost:8000"+prof_user.Image.url
    user_dict['posts'] = []
    user_dict['cur_user'] = var[0].username
    user_dict['is_followed'] = False
    user_dict['allowed'] = allowed
    user_dict["background_image"]="http://localhost:8000"+prof_user.Image_background.url
    check_rln = FriendRequest.objects.raw("SELECT * FROM home_FriendRequest WHERE sender_username='"+str(
        req_username)+"' AND receiver_username='"+var[0].username+"'")
    
    # make profile public 
    if user_dict['followers'] >= 1000:
        user_dict['allowed'] = True
        
    print(len(check_rln))
    if len(check_rln) >= 1:
        user_dict['is_followed'] = True
        for i in check_rln:
            print(i.get_followed())
            if i.get_followed() == True:
                user_dict['accepted'] = True
            else:
                user_dict['accepted'] = False
    for p in posts:
        user_post_obj = {}
        user_post_obj['photo_url'] = "http://localhost:8000/media/"+p.photo_url
        user_post_obj['post_id'] = p.post_id
        user_post_obj['likes'] = len(likes.objects.filter(post_id=p.post_id))
        # Add here one for comment
        user_post_obj['comments'] = 30
        user_dict['posts'].append(user_post_obj)
    # print(user_dict)
    return render(request, 'home/show_users.html', user_dict)

    # return HttpResponse("lol")


def add_post(request):
    if request.method == 'POST':
        form = ImageFrom(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data['Caption'])
            # print(form.cleaned_data['Image'])
            img = form.cleaned_data['Image']
            caption = form.cleaned_data['Caption']
            location = form.cleaned_data['Location']
            cur_user = request.user
            print(cur_user)
            # print(img.open())
            timestamp = str(datetime.timestamp(datetime.now()))
            path = default_storage.save(
                'home/posts_images/'+timestamp+'.jpg', ContentFile(img.read()))
            print(type(path))
            user_post = post(user_fk=cur_user, photo_url=path, is_reported=False,
                             location=location, date_posted=datetime.date(datetime.now()), caption=caption)
            user_post.save()
            # tmp_file = os.path.join(settings.MEDIA_ROOT, path)
            return redirect("http://localhost:8000/home")
        else:
            print("invalid")
        return HttpResponse("YAY")

    else:
        form = ImageFrom()
    return render(request, 'home/add_post_1.html', {'form': form})


@csrf_exempt
def add_friend(request):
    # print(request.POST)
    option = request.POST['option']
    print(option)

    destination_user = request.POST['destination_user']
    # print(destination_user)
    destination_user_auth = User.objects.filter(username=destination_user)
    # print(destination_user_auth)
    if(option == "unfriend"):
        request_obj = FriendRequest.objects.filter(
            sender_username=request.POST['sender_username'], receiver_username=destination_user)
        request_obj.delete()

    else:
        request_obj = FriendRequest(
            sender_username=request.POST['sender_username'], receiver_username=destination_user)
        request_obj.save()
    # return response
    return HttpResponse("add friend")


@csrf_exempt
def add_friend_status(request):
    sender_name = request.POST['sender_username']
    reciever_name = request.POST['rec_name']
    status = request.POST['option']
    check_rln = FriendRequest.objects.raw(
        "SELECT * FROM home_FriendRequest WHERE sender_username='"+sender_name+"' AND receiver_username='"+reciever_name+"'")
    if status=="accept":
        add_notification(reciever_name + " accepted your request.","",User.objects.filter(username=sender_name)[0])
        if len(check_rln) >= 1:
            for req in check_rln:
                req.request_status = True
                print(req)
                req.save()
    else:
        for req in check_rln:
            req.delete()
            
    return HttpResponse("skcksn")


def showFollowers(request, slug):
    followers = FriendRequest.objects.filter(
        receiver_username=slug, request_status=True)
    # print(len(followers))
    friend_list = {}
    friend_list['friend'] = []
    friend_list['cur_user'] = slug
    for user in followers:
        cur_user = customuser.objects.filter(
            user_inher__username=user.sender_username)[0]
        temp = {}
        temp['username'] = user.sender_username
        temp['image'] = 'http://localhost:8000'+cur_user.Image.url
        friend_list['friend'].append(temp)

    # print(friend_list)

    return render(request, 'home/show_followers.html', friend_list)


def showFollowing(request, slug):
    followers = FriendRequest.objects.filter(sender_username=slug, request_status=True)
    # print(len(followers))
    friend_list = {}
    friend_list['friend'] = []
    friend_list['cur_user'] = slug
    for user in followers:
        cur_user = customuser.objects.filter(
            user_inher__username=user.receiver_username)[0]
        temp = {}
        temp['username'] = user.receiver_username
        temp['image'] = 'http://localhost:8000'+cur_user.Image.url
        friend_list['friend'].append(temp)

    # print(friend_list)

    return render(request, 'home/show_following.html', friend_list)


def logout_view(request):
    logout(request)
    return redirect('http://localhost:8000/')

@csrf_exempt
def removeNotifications(request):
    if request.method=="POST":
        notif_id=request.POST["notif_id"]
        notification=Notifications.objects.filter(notif_id=notif_id)
        notification.delete()
        return HttpResponse("Notification deleted")
    else:
        return HttpResponse("<h1>Page not found</h1>")
    

def settings(request):
    return render(request,"home/settings.html")

def delete_ac(request):
    cur_user=request.user
    secret_key=random.randint(10000,99999)
    # objs=user_secret_key.objects.filter(user_fk=cur_user)
    cust_cur_user=customuser.objects.filter(user_inher=cur_user)[0]
    
        # Make new Key
    ukey=user_secret_key(user_fk=cur_user,secret_key=secret_key)
        
    ukey.save()
        
    sending_mail("Delete account on SocialHub","computerdummy960@gmail.com",cust_cur_user.email,"Use this key here","<h3>Your key to delete the account is:</h3><br><h1>"+str(secret_key)+"</h1><br>") 
    print("After send mail")
    return render(request,"home/delete_ac_verify.html")    

def delete_verify_ac(request):
    cur_user=request.user
    user_key_objs=user_secret_key.objects.filter(user_fk=cur_user).order_by("date_valid").reverse()[0]

    if request.POST["key"]==str(user_key_objs.secret_key):
        cur_user.delete()
        user_key_objs.delete()
        return redirect("http://localhost:8000")
        print("here")
    else:
        user_key_objs.delete()
        return redirect("http://localhost:8000/home")
    
    
    # return render(request,"home/delete_ac_verify.html")




def edit_post(request):
    if request.method=="GET":
        posts=getPostByUser(request.user)
        ret_dict={}
        ret_dict["post_data"]=[]
        for i in posts:
            ret_dict["post_data"].append(i)
        print(ret_dict)
        return render(request,'home/edit_post.html',ret_dict) 
    else:
        posts=getPostByUser(request.user)
        for i in posts:
            if str(i.post_id) in request.POST:
                post_fetch=post.objects.filter(post_id=i.post_id)[0]
                print(post_fetch)
                post_fetch.delete()
                notifcation=Notifications(notif_title="You deleted a post",notify_to=request.user,notif_msg="You deleted a post msg")
                notifcation.save()
        messages.add_message(request,messages.INFO,"You delted post")
        return redirect("http://localhost:8000/home/profile")

def add_profile_image(request):
    print(request.method)
    if request.method=="POST":
        form = UserProfilImage(request.POST, request.FILES)
        print("Herrrrrr")
        if form.is_valid():
            img = form.cleaned_data['Image']
            timestamp = str(datetime.timestamp(datetime.now()))
            path = default_storage.save(
                'home/user_images/'+timestamp+'.jpg', ContentFile(img.read()))
            # tmp_file = os.path.join(settings.MEDIA_ROOT, path)
            print(path)
            cust_user=customuser.objects.filter(user_inher=request.user)[0]
            cust_user.Image=path
            cust_user.save()
            print("here")
            return redirect("http://localhost:8000/home/profile")
    print("jeni")
    form=UserProfilImage()
    return render(request,'home/profile_image.html',{'form':form})

def add_backround_image(request):
    print(request.method)
    if request.method=="POST":
        form = UserProfilImage(request.POST, request.FILES)
        print("Herrrrrr")
        if form.is_valid():
            img = form.cleaned_data['Image']
            timestamp = str(datetime.timestamp(datetime.now()))
            path = default_storage.save(
                'home/user_background_images/'+timestamp+'.jpg', ContentFile(img.read()))
            # tmp_file = os.path.join(settings.MEDIA_ROOT, path)
            print(path)
            cust_user=customuser.objects.filter(user_inher=request.user)[0]
            cust_user.Image_background=path
            cust_user.save()
            print("here")
        return redirect("http://localhost:8000/home/profile")
    print("jeni")
    form=UserProfilImage()
    return render(request,'home/backround_image.html',{'form':form})
