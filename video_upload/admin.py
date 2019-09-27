from django.contrib import admin
from .models import Television, Document

admin.site.register(Television) #import the Television model from models.py
admin.site.register(Document) #import the Document model from models.py

# class Document(admin.ModelAdmin):
#     readonly_fields=('video_id','upload_date')