from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=32)
    image = models.CharField(max_length=32, default='')