from django.shortcuts import render,HttpResponse

def index(request):
    return render(request,"search/search.html")

def search_query(request):
    print(request.POST['search_query'])
    return HttpResponse("Got search as "+str(request.POST['search_query']))
