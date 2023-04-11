from django.urls import path
from . import views

urlpatterns = [
    path('/Users/kate/Desktop/Fleur/fleur_api/plants_api', views.PlantList.as_view(), name='plant_list'),
    path('/Users/kate/Desktop/Fleur/fleur_api/plants_api/<int:pk>', views.PlantDetail.as_view(), name='plant_detail')
]