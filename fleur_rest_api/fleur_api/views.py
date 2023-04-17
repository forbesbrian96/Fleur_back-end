from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .serializers import PlantSerializer
from .models import Plant
from rest_framework.response import Response
from django.shortcuts import redirect

# Create your views here.
class PlantList(generics.ListCreateAPIView):
    queryset = Plant.objects.all().order_by('id')
    serializer_class = PlantSerializer


class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all().order_by('id')
    serializer_class = PlantSerializer


def rate(request, plant_id: int, rating: int) -> HttpResponse:
    plant = Plant.objects.get(id=plant_id)
    Rating.objects.filter(plant=plant, user=request.user).delete()
    plant.rating_set.create(user=request.user, rating=rating)
    return HttpResponseRedirect('/')



