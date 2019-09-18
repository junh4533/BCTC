from django.db import models
from datetime import datetime
import subprocess
import shutil, os

class Television(models.Model):
    tv_id = models.AutoField(primary_key=True)
    tv_ip = models.GenericIPAddressField(unpack_ipv4=True)
    tv_name = models.CharField(max_length=50, blank=False)
    def __str__(self):
        return self.tv_name

class Document(models.Model):
    video_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255, blank=True)
    # tv = models.OneToOneField(Television, on_delete=models.CASCADE)
    tv = models.ForeignKey(Television, on_delete=models.CASCADE)
    
    def delete_file(path):
        if os.path.isfile(path):
            os.remove(path)
            print('File deleted')

    # def file_path(self, tv):
    #     # removes the original file
    #     path =  "C:/Users/Administrator/Desktop/Django Projects/BCTC/media/videos/" + self.tv + ".mp4"
    #     # copy video files to another directory
    #     #dst = "C:/Users/Administrator/Desktop/Django Projects/BCTC/media/test/" +self.tv +".mp4"
    #     #shutil.copy(path, dst, follow_symlinks=True)
    #     if os.path.isfile(path):
    #         os.remove(path)
    #         print('File deleted')
    #         print(self.tv)
    #     return 'videos/' + self.tv + ".mp4"

    def file_path(self, tv):
        # removes the original file
        path =  "C:/Users/Administrator/Desktop/Django Projects/BCTC/media/videos/" + str(self.tv) + ".mp4"
        # copy video files to another directory
        #dst = "C:/Users/Administrator/Desktop/Django Projects/BCTC/media/test/" +self.tv +".mp4"
        #shutil.copy(path, dst, follow_symlinks=True)
        if os.path.isfile(path):
            os.remove(path)
            print('File deleted')
            print(self.tv)
        return 'videos/' + str(self.tv) + ".mp4"

    # gives the objects its file name
    def __str__(self):
        return str(self.tv) + " (Date Uploaded: " + str(datetime.now()) + ")"

    document = models.FileField(upload_to= file_path)
    upload_date = models.DateTimeField(auto_now_add=True)




    

    
    
