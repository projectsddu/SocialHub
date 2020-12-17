from django.shortcuts import render,HttpResponse
from home.models import likes
from django.db.models.expressions import RawSQL

def index(request):
    return render(request,"search/search.html")

def search_query(request):
    print(request.POST['search_query'])
    # x=likes.objects.all()
    # Operational Error: No column found Post_id
    # x=likes.get_treding()
    x=likes.objects.raw("Select like_id,post_id_id, count(post_id_id) as cpid From home_likes where date_liked='2020-12-17'  Group by post_id_id Order by count(post_id_id) DESC;")
    print(len(x))
    for i in x:
        print(i.cpid,i.post_id)
    return render(request,'search/search_query_page.html')



# render this in render
# query for trending
# Select pid, count(pid)
# From likes
# Where date_added = '16-dec-20'
# Group by pid
# Order by count(pid) DESC;