from django.shortcuts import render,HttpResponse
from home.models import FriendRequest,likes,post
from django.views.decorators.csrf import csrf_exempt
from datetime import date
from datetime import timedelta
from django.http import JsonResponse
from django.contrib.auth.models import User
from home.views import getLikesByPost
# Create your views here.
def index (request):
    return render(request,'business_dashboard/base.html')

def business(request):
    return render(request,'business_dashboard/business_details.html')

def advertise(request):
    return render(request,"business_dashboard/advertise.html")


@csrf_exempt
def getFollowers(request):
    if request.method=="POST":
        ret_dict={}
        cul_ret_list=[]
        today=date.today()
        ret_list=[]
        for i in range(0,6):
            query=FriendRequest.objects.filter(date=today-timedelta(days=i),receiver_username=request.POST["username"])
            ret_list.append(len(query))
            if i==0:
                cul_ret_list.append(len(query))
            else:
                cul_ret_list.append(cul_ret_list[i-1]+len(query))
        print(ret_list)
        ret_dict["followers"]=ret_list
        ret_list=[]
        ret_dict["monthly"]=cul_ret_list
        cur_user=User.objects.filter(username=request.POST["username"])[0]
        query=post.objects.filter(user_fk=cur_user).order_by("date_posted")
        date_list=[]
        for i in query:
            ret_list.append(getLikesByPost(i,cur_user,True))
            date_list.append(i.date_posted)
        print(ret_list)
        ret_dict["likes"]=ret_list
        ret_dict["like_labels"]=date_list
        print(ret_dict)
        return JsonResponse(ret_dict)
    else:
        return HttpResponse("<h1> Error</h1>")