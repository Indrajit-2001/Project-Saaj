from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.
class Mehndigallery(models.Model):
    photo=models.FileField(upload_to='Mehndi_gallery/',max_length=500,null=True,default=None)
    info=models.CharField(max_length=100)