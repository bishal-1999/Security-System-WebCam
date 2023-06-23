from django.contrib import admin
from django.urls import path
from .views import *

app_name='blog'

urlpatterns = [
    path('',welcome,name='welcome'),
    path('signup',signup_view,name='signup'),
    path('login',login_view,name='login'),
    path('home',home,name='home'),
    path('logout',logout_view,name='logout'),
    path('option1',option_1,name='option1'),
     path('myview',my_view,name='myview'),


]