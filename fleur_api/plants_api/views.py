
from rest_framework import generics
from .serializers import PlantSerializer 
from .models import Plant 

class PlantList(generics.ListCreateAPIView):
    queryset = Plant.objects.all().order_by('id')
    serializers_class = PlantSerializer 

class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all().order_by('id')
    serializer_class = PlantSerializer
