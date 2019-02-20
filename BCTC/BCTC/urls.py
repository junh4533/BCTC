"""BCTC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

looks at the requested url and decides which function to run in views.py 
"""
from video_upload import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

#connect to the url.py in the app
#r=route ^=start with $=end with
urlpatterns = [
    url(r'^$', include('video_upload.urls')),
    url(r'^admin/', admin.site.urls), 
    url(r'^accounts/', include('django.contrib.auth.urls')), #login and logout
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
