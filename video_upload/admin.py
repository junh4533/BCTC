from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Television, Document
admin.site.register(Television) #import the Television model from models.py
admin.site.register(Document) #import the Document model from models.py

# class Document(admin.ModelAdmin):
#     readonly_fields=('video_id','upload_date')
class UserAdmin(admin.ModelAdmin):
    def queryset(self, request):
        if request.user.is_super:
            return User.objects.filter(is_superuser=False)
        return User.objects.filter(is_superuser=False)