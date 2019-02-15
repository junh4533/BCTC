from django.db import models

tv_choices = (
    ('TV1','TV1'),
    ('TV2','TV2'),
    ('TV3','TV3'),
    ('TV4','TV4'),
)
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='videos')
    tv = models.CharField(max_length=3,
        choices = tv_choices,default='TV1'
    )
    upload_date = models.DateTimeField(auto_now_add=True)
