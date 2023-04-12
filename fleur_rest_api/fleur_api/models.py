from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=32, default='')
    image = models.CharField(max_length=200, default='') 
    notes = models.CharField(max_length=200, default='') 
