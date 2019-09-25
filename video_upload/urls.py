# app url

from django.conf.urls import url, include
from django.urls import path
from . import views

#load methods from views.py
urlpatterns = [
    path('', views.index, name='index'), #load a method called index from views.py
    path('add_tv/', views.add_tv, name='add_tv'), #load a method called add_tv from views.py
    path('config_tv/', views.config_tv, name='config_tv'),
    path('edit_tv/', views.edit_tv, name='edit_tv')
    # path('upload/',views.upload,name='upload'),
]