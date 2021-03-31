from django.shortcuts import render,HttpResponse
from home.models import post,comments,FriendRequest
from login.models import customuser 
from home.views import getCommentsByPosts,getLikesByPost

def view_post(request,slug):
    
    post_display = post.objects.filter(post_id=slug)[0]
    post_caption=post_display.caption
    post_owner = post_display.user_fk.username
    photo_url = "http://localhost:8000/media/"+post_display.photo_url
    # print(post_url)
    # print(post_display)
    comment_list = getCommentsByPosts(slug,True)
    likes = getLikesByPost(post_display,request.user)
    display_dict = {
        'comments': comment_list,
        'likes': likes,
        'owner': post_owner,
        'date_added': post_display.date_posted,
        'photo_url': photo_url,
        'caption':post_caption
    }
    if request.user.username==post_owner:
        return render(request,'ViewPost/index.html',display_dict)

    if check_relation(request.user.username, post_owner) == False :
        return HttpResponse("You are not allowed!!!!")
    
        
    return render(request,'ViewPost/index.html',display_dict)

def check_relation(sender,receiver):
    f1 = FriendRequest.objects.filter(sender_username = sender, receiver_username = receiver, request_status = True)
    f2 = FriendRequest.objects.filter(sender_username = receiver, receiver_username = sender, request_status = True)
    # print("------------------------------")
    # print(f1,f2)
    if len(f1) != 0 or len(f2) != 0:
        return True
    else:
        return False