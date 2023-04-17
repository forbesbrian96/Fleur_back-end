from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



class Plant(models.Model):
    header = models.CharField(max_length=32, default='')
    image = models.CharField(max_length=200, default='') 
    text = models.TextField(default='') 
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.header

