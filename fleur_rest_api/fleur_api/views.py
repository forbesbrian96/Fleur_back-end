from django.shortcuts import render
from rest_framework import generics
from .serializers import PlantSerializer
from .models import Plant

# Create your views here.
class PlantList(generics.ListCreateAPIView):
    queryset = Plant.objects.all().order_by('name')
    serializer_class = PlantSerializer

class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all().order_by('name')
    serializer_class = PlantSerializer