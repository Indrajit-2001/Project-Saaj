from django.db import models

# Create your models here.
class Partylookgallery(models.Model):
    photo=models.FileField(upload_to="party_look_gallery/",max_length=500,null=True,default=None)
    info=models.CharField(max_length=100)