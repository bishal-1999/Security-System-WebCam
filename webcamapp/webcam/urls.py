from django.urls import path
from .views import *

app_name='webcam'

urlpatterns = [
    path('',welcome,name='welcome'),
    path('option1',option1,name='option1'),
    path('option2',option2,name='option2'),
  #('option3',option3,name='option3'),
   # path('option4',option4,name='option4'),
   # path('option5',option5,name='option5'),
   #path('option6',option6,name='option6'),
  # path('option7',option7,name='option7'),
   # path('option8',option8,name='option8'),
]