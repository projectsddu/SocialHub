from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages
from .models import customuser
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives




def login(request):
    return render(request,'login/base.html')

@csrf_exempt
def login_user(request):
    if request.method=='GET':
        return HttpResponse("<h1>ERROR 404 PAGE NOT FOUND</h1>")
    else:
        email=request.POST.get('login')
        password=request.POST.get('password')
        user = authenticate(request,username=email, password=password)
        if user is not None:
            auth_login(request,user)
            print("jenil logged in")
            return redirect('http://localhost:8000/home')
        else:
            print("check login or password details")
    return HttpResponse("4040")

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        
        if check_user_name(username) != None:
            messages.warning(request,'Username is already taken!!!')
            return render(request,'login/signup.html')
        city = request.POST.get('city')
        country = request.POST.get('country')
        bio = request.POST.get('bio')
        password = request.POST.get('password')
        #check both are same or not
        c_password = request.POST.get('c_password')
        #print(username, city, country, bio, password, c_password)
        user = User.objects.create_user(username, 'lennon@thebeatles.com', password)
        user.save()
        custom_user = customuser (city_of_residence = city, country_of_residence = country, bio = bio, user_inher = user)
        custom_user.save()
        user = authenticate(request,username=username, password=password)
        if user is not None:
            auth_login(request,user)
            print("jenil logged in")
            return redirect('http://localhost:8000/home')
        else:
            print("check login or password details")
        return redirect('http://localhost:8000/home')
         
    return render(request,'login/signup.html')

def check_password(password1,password2):
    if password1 == password2:
        return True
    else:
        return False


def check_user_name(username):
    user = User.objects.filter(username = username)
    if len(user) == 0:
        return None
    return (user)


def forgot_password(request):
    if request.method=="POST":
        username=request.POST["username"]
        print(username)
        # message=render_to_string(template_name="login/forgot_template.html")
        # send_mail(
        #     'Subject here',
        #     message,
        #     'computerdummy960@gmail.com',
        #     ['confusedjogger01@gmail.com'],
        #     fail_silently=False,
        # )
        subject, from_email, to = 'hello', 'computerdummy960@gmail.com', 'confusedjogger01@gmail.com'
        text_content = 'This is an important message.'
        html_content = '<h1>Jenil Gandhi</h1>'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return HttpResponse("submitted")
    return render(request,'login/forgot_password.html')