from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

#regex:
    #r=route ^=start with $=end with nothing

#load methods from views.py
urlpatterns = [
    url(r'^$', views.index, name='index') #load a method called index from views.py
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)