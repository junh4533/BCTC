# app url

from django.conf.urls import url, include
from django.urls import path
from . import views

#load methods from views.py
urlpatterns = [
    path('', views.index, name='index'), #load a method called index from views.py
    path('video1/', views.video1, name='video1'), #load a method called index from views.py
    path('video2/', views.video2, name='video2'), #load a method called index from views.py
    path('video3/', views.video3, name='video3'), #load a method called index from views.py
    path('video4/', views.video4, name='video4'), #load a method called index from views.py
]