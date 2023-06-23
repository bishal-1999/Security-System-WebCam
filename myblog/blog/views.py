from django.shortcuts import render,redirect
from django.http import *
from django.contrib.auth import *
from django.contrib import messages
from django.contrib.auth.models import *
from django.contrib.auth.forms import *
from .forms import *
import cv2

def welcome(request):
     return render(request,'welcome.html',)
def signup_view(request):
    if request.method == "POST":
       form = SignUpForm(request.POST)
       if form.is_valid():
          messages.success(request, 'Congratulations!! You have become an Author.')
          user = form.save()
    else:
       form = SignUpForm()
    return render(request, 'signup.html', {'form':form})
def login_view(request):
   if request.method == "POST":
         form = LoginForm(request=request, data=request.POST)
         if form.is_valid():
          uname = form.cleaned_data['username']
          upass = form.cleaned_data['password']
          user = authenticate(username=uname, password=upass)
          if user is not None:
            login(request, user)
            return redirect('/blog/home')
   else:
      form = LoginForm()
   return render(request, 'login.html', {'form':form})

def home(request):
 if request.user.is_authenticated:
  user = request.user
  full_name = user.get_full_name()
  return render(request, 'home.html', {'full_name':full_name})
 else:
  return redirect('/blog/login')

def option_1(request):
    cam = cv2.VideoCapture(0)
    while cam.isOpened():
       ret, frame1 = cam.read()
       if cv2.waitKey(10) == ord('q'):
          break
    cv2.imshow('Granny Cam', frame1)
    return HttpResponse("")

def my_view(request):
    # Your integration logic here
    result = option_1(request)  # Call your Python function or code here

    return HttpResponse(result)


def logout_view(request):
    logout(request)
    return redirect('/blog/login')

