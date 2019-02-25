from django.db import models
from datetime import datetime
import os


tv_choices = (
    ('TV1','TV1'),
    ('TV2','TV2'),
    ('TV3','TV3'),
    ('TV4','TV4'),
)


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    # document = models.FileField(upload_to='videos/')
    tv = models.CharField(max_length=3,
        choices = tv_choices,default='TV1'
    )
    
    def delete_file(path):
        if os.path.isfile(path):
            os.remove(path)
            print('File deleted')

    def file_path(self, tv):
        # removes the original file
        path =  "C:\\Users\Administrator\Desktop\Django Projects\BCTC\media\\videos\\" + self.tv + ".mp4"
        if os.path.isfile(path):
            os.remove(path)
            print('File deleted')
        return 'videos/' + self.tv + ".mp4"
    
    # gives the objects its file name
    def __str__(self):
        return self.tv + " (Date Uploaded: " + str(datetime.now()) + ")"

    document = models.FileField(upload_to= file_path)
    upload_date = models.DateTimeField(auto_now_add=True)

    
    
