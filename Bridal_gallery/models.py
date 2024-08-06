from django.db import models

# Create your models here.
class Bridalgallery(models.Model):
    photo=models.FileField(upload_to="bridal_gallery/",max_length=500,null=True,default=None)
    info=models.CharField(max_length=100)