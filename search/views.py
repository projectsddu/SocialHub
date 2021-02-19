from django.shortcuts import render, HttpResponse
from home.models import likes
from django.db.models.expressions import RawSQL
from django.http import JsonResponse
from login.models import customuser
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, "search/search.html")

def search_query(request):
    print(request.POST.get('search_query'))

    # x=likes.objects.all()
    # Operational Error: No column found Post_id
    # x=likes.get_treding()
    x = likes.objects.raw(
        "Select like_id,post_id_id, count(post_id_id) as cpid From home_likes where date_liked='2020-12-17'  Group by post_id_id Order by count(post_id_id) DESC;")
    print(len(x))
    for i in x:
        print(i.cpid, i.post_id)
    return render(request, 'search/search_query_page.html')

@csrf_exempt
def search_user(request):
    
    # print(request.GET.get('data'))
    mydict={}
    print(request.POST)
    # data=request.POST
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
    # for key in data.iterKeys():
    #     mydict[key]=data.getlist(key)
    if final_data=="":
        return {'post':[]}
    # print(mydict)
    # mydict=dict(data.iterlists())
    # data=json.loads(request.POST)
    # search_result = customuser.objects.filter(user_inher__username=final_data)
    search_result1 = customuser.objects.filter(user_inher__username__startswith=final_data)
    results = {'post': []}
    # for i in search_result:
    #     temp = {}
    #     temp['username'] = i.user_inher.username
    #     temp['photo_url'] = i.Image.url
    #     results['post'].append(temp)
    
    for i in search_result1:
        temp = {}
        temp['username'] = i.user_inher.username
        temp['photo_url'] = i.Image.url
        results['post'].append(temp)
        
    return JsonResponse(results)


# render this in render
# query for trending
# Select pid, count(pid)
# From likes
# Where date_added = '16-dec-20'
# Group by pid
# Order by count(pid) DESC;
