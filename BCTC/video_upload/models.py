from django.db import models
from datetime import datetime

# Create your models here.
class Video(models.Model):
    file_name = models.CharField(max_length=200, blank=True)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    # test_field = models.CharField(max_length=200, blank=True) 
    
    #name each object (video) its file_name
    def __str__(self): 
        return self.file_name