from django.conf.urls import url, include
from . import views

#regex:
    #r=route ^=start with $=end with nothing

#load methods from views.py
urlpatterns = [
    url(r'^$', views.index, name='index'), #load a method called index from views.py
]