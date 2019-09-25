from django.db import models
from datetime import datetime
import subprocess
import shutil, os

class Television(models.Model):
    tv_id = models.AutoField(primary_key=True)
    tv_ip = models.GenericIPAddressField(unpack_ipv4=True)
    tv_name = models.CharField(max_length=50, blank=False,unique=True)
    def __str__(self):
        return self.tv_name

#Pass the key from Television Table to create a drop down in template
class Config(models.Model):
    TV = models.ForeignKey(Television, on_delete=models.CASCADE)

class Document(models.Model):
    def file_path(self, tv):
        # removes the original file
        path =  "C:/Users/Administrator/Desktop/Django Projects/BCTC/media/videos/" + str(self.tv) + ".mp4"
        if os.path.isfile(path):
            os.remove(path)
            print('File deleted')
            print(self.tv)
        return 'videos/' + str(self.tv) + ".mp4"

    def delete_file(path):
        if os.path.isfile(path):
            os.remove(path)
            print('File deleted')

    video_id = models.AutoField(primary_key=True)
    document = models.FileField(upload_to=file_path)
    upload_date = models.DateTimeField(auto_now_add=True)
    tv = models.ForeignKey(Television, on_delete=models.CASCADE)

    # gives the objects its file name
    def __str__(self):
        return str(self.tv) + " (Date Uploaded: " + str(datetime.now()) + ")"

    




    

    
    
