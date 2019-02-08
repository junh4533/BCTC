from django.contrib import admin

# Register your models here.
from .models import Video
admin.site.register(Video) #import the Videos model from models.py