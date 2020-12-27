from django.db import models
from datetime import datetime


class Listing(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    photo_main=models.ImageField(upload_to='photos/%y/%m/%d/')
    photo_1=models.ImageField(upload_to='photos/%y/%m/%d/',blank=True)
    photo_2=models.ImageField(upload_to='photos/%y/%m/%d/',blank=True)
    photo_3=models.ImageField(upload_to='photos/%y/%m/%d/',blank=True)
    is_published=models.BooleanField(default=True)
    list_date=models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.title

# Create your models here.
