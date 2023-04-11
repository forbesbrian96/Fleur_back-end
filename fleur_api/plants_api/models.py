from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=32)
    image = models.CharField(max_length=100, default="Unknown")