from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_plants, name='plants'),
    path('<plant_id>', views.plant_detail, name='plant_detail'),
]
