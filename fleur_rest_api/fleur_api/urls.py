from django.urls import path
from . import views

urlpatterns = [
    path('api/plants', views.PlantList.as_view(), name='plant_list'), 
    path('api/plants/<int:pk>', views.PlantDetail.as_view(), name='plant_detail'), 
]
