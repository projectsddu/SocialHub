from django.shortcuts import render,HttpResponse

# Create your views here.
def index (request):
    return render(request,'business_dashboard/base.html')

def business(request):
    return render(request,'business_dashboard/business_details.html')

def advertise(request):
    return render(request,"business_dashboard/advertise.html")