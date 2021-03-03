import os
from .models import post, likes
from login.models import customuser
from .forms import ImageFrom
from .models import UploadImage, post, FriendRequest,Notifications,comments
from datetime import datetime
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


def getfollowers(username):
    query = FriendRequest.objects.filter(
        receiver_username=username, request_status=True)
    return len(query)


def getfollowing(username):
    query = FriendRequest.objects.filter(
        sender_username=username, request_status=True)
    return len(query)


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


def getLikesByPost(post_obj, cur_user):
    like = likes.objects.filter(post_id=post_obj.post_id)
    like_count = len(like)
    you = likes.objects.filter(post_id=post_obj.post_id, liker_user=cur_user)
    if len(you) == 1:
        return "You and "+str(like_count-1)+" other"
    return str(like_count)+" people"


def get_notifs(user):
    query=Notifications.objects.filter(notify_to=user)
    notification=[]
    for cur_query in query:
        cur_dict={}
        cur_dict['message']=cur_query.notif_msg
        cur_dict["title"]=cur_query.notif_title
        cur_dict['date']=cur_query.date_added
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
    posts_query = post.objects.all().order_by('post_id').reverse()
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
        user_image_url = current_user_profile[0].Image.url
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
                              'image_url': image_url, 'post_id': i.post_id, 'poster_image_url': user_image_url, 'comments': getCommentsByPosts(i), 'isliked': final_bool})
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
        # print(type(post_given[0]))
        liker = User.objects.filter(username=liker)[0]
        like_given = likes(post_id=post_given, liker_user=liker)
        like_given.save()
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
    posts = post.objects.filter(user_fk=var[0]).order_by("post_id").reverse()
    no_of_posts = len(posts)
    user_dict['n_posts'] = no_of_posts
    user_dict['following'] = getfollowing(prof_user.user_inher.username)
    user_dict['followers'] = getfollowers(prof_user.user_inher.username)
    user_dict['user_image'] = "http://localhost:8000"+prof_user.Image.url
    user_dict['posts'] = []
    user_dict['cur_user'] = var[0].username
    user_dict['is_followed'] = False
    check_rln = FriendRequest.objects.raw("SELECT * FROM home_FriendRequest WHERE sender_username='"+str(
        req_username)+"' AND receiver_username='"+var[0].username+"'")

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
            tmp_file = os.path.join(settings.MEDIA_ROOT, path)
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
