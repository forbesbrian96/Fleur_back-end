from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/plants', views.PlantList.as_view(), name='plant_list'), 
    path('api/plants/<int:pk>', views.PlantDetail.as_view(), name='plant_detail'), 
    path('rate/<int:plant_id>/<int:rating>/', views.rate),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
