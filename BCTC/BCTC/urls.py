# project url

from video_upload import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

#connect to the url.py in the app
urlpatterns = [
    url(r'', include('video_upload.urls')),
    url(r'^admin/', admin.site.urls), 
    url(r'^accounts/', include('django.contrib.auth.urls')), #login and logout   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
