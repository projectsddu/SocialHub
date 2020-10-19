from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
def index(request):
    user_name=request.user
    print(user_name.username)
    user_details_dict={
        'name':str(user_name.username)
    }
    return render(request,'home/home.html',user_details_dict)

@csrf_exempt
def add_like_to_post(request):
    if request.method =='POST':
        print(request.POST)
        return HttpResponse("recieved post")
    else:
        return HttpResponse("<h1>404 Page not found</h1>")

@csrf_exempt
def add_unlike_to_post(request):
    if request.method =='POST': 
        print(request.POST)
        return HttpResponse("recieved post")
    else:
        return HttpResponse("<h1>404 Page not found</h1>")

@csrf_exempt
def comment(request):
    json_data={'comments':[
        {'user_1':'jenil is a boy'},
        {'user_1':'jenil is a boy'},
        {'user_1':'jenil is a boy'},
        {'user_1':'jenil is a boy'},
    ]}
    print(request.POST)
    return JsonResponse(json_data)
def search(request):
    #let us consider that the search user 
    json_data={
        'users':[
            {
                'name':'Jenik Vekariya',
                'photo':'https://source.unsplash.com/1600x900/?nature,mountain',
                'occupation':'SDE at Google'
            },
            {
                'name':'Harshvardhan Sharma',
                'photo':'https://source.unsplash.com/1600x900/?nature,water',
                'occupation':'SDE at Amazon'
            }
        ]
    }
    return JsonResponse(json_data)