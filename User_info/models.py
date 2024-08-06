from django.db import models

# Create your models here.
class User_info(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    phone=models.CharField(max_length=10)
    date=models.DateField(max_length=10)