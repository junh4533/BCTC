# app url

from django.conf.urls import url, include
from django.urls import path
from . import views

#load methods from views.py
urlpatterns = [
    path('', views.index, name='index'), #load a method called index from views.py
    path('add_tv/', views.add_tv, name='add_tv'), #load a method called add_tv from views.py
    path('delete_tv/', views.delete_tv, name='delete_tv')
    # path('upload/',views.upload,name='upload'),
]