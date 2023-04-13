from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Plant(models.Model):
    header = models.CharField(max_length=32, default='')
    image = models.CharField(max_length=200, default='') 
    text = models.TextField(default='') 

def average_rating(self) -> float:
        return Rating.objects.filter(plant=self).aggregate(Avg("rating"))["rating__avg"] or 0

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.plant.header}: {self.rating}"

    
