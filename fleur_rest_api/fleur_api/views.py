from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .serializers import PlantSerializer
from .models import Plant, Rating
from rest_framework.response import Response
from django.shortcuts import redirect

# Create your views here.
class PlantList(generics.ListCreateAPIView):
    queryset = Plant.objects.all().order_by('id')
    serializer_class = PlantSerializer


class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all().order_by('id')
    serializer_class = PlantSerializer

    def get(self, request, *args, **kwargs):
        plants = self.get_queryset()
        for plant in plants:
            rating = Rating.objects.filter(plant=plant, user=request.user).first()
            plant.user_rating = rating.rating if rating else 0
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)


def rate(request, plant_id: int, rating: int) -> HttpResponse:
    plant = Plant.objects.get(id=plant_id)
    Rating.objects.filter(plant=plant, user=request.user).delete()
    plant.rating_set.create(user=request.user, rating=rating)
    return HttpResponseRedirect('/')


# Overview. *args specifies the number of non-keyworded arguments that can be passed and the operations that can be performed on the function in Python whereas **kwargs is a variable number of keyworded arguments that can be passed to a function that can perform dictionary operations.