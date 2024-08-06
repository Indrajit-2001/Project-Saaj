from email.policy import default
from django.db import models

# Create your models here.

class Artgallery(models.Model):
    photo=models.FileField(upload_to="art_gallery/",max_length=500,null=True,default=None)
    info=models.CharField(max_length=100)
