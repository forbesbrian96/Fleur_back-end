from rest_framework import serializers 
from .models import Plant

class PlantSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Plant # tell django which model to use
        fields = '__all__' # tell django which fields to include
