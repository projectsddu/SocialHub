from django.shortcuts import render, HttpResponse
from home.models import likes,post
from django.db.models.expressions import RawSQL
from django.http import JsonResponse
from login.models import customuser
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from home.views import getCommentsCount

def check_datetime(obj):
    if len(str(obj))==1:
        return "0"+str(obj)
    else:
        return str(obj)

def index(request):
    year=datetime.datetime.now().year
    day=datetime.datetime.now().day
    month=datetime.datetime.now().month
    today=str(year)+"-"+str(check_datetime(month))+"-"+str(check_datetime(day))
    x = likes.objects.raw(
        "Select like_id,post_id_id, count(post_id_id) as cpid From home_likes where date_liked='"+today+"'  Group by post_id_id Order by count(post_id_id) DESC;")
    print(len(x))
    post_details={}
    post_details['posts']=[]
    for i in x:
        post_tmp={}
        posts=post.objects.filter(post_id=i.post_id.post_id)[0]
        post_tmp['url']="http://localhost:8000/media/"+posts.photo_url
        post_tmp['likes']=len(likes.objects.filter(post_id=posts.post_id))
        post_tmp['comments']=getCommentsCount(i.post_id.post_id)
        # post_tmp["post_id"]=posts.post_id
        post_details['posts'].append(post_tmp)
    return render(request, "search/search.html",post_details)

def search_query(request):
    print(request.POST.get('search_query'))

    
    return render(request, 'search/search_query_page.html')

@csrf_exempt
def search_user(request):
    
    
    mydict={}
    print(request.POST)
    
    queryDict=request.POST
    myDict = {}
    for key in queryDict.keys():
        myDict[key] = queryDict.getlist(key)
    cntr=1
    our_data=1
    for key in myDict:
        if cntr==2:
            break
        else:
            our_data=key
    mydata=json.loads(our_data)

    final_data=mydata['data']    
    print(final_data)
    
    if final_data=="":
        return {'post':[]}
   
    search_result1 = customuser.objects.filter(user_inher__username__startswith=final_data)
    results = {'post': []}
      
    for i in search_result1:
        temp = {}
        temp['username'] = i.user_inher.username
        temp['photo_url'] = i.Image.url
        results['post'].append(temp)
        
    return JsonResponse(results)


