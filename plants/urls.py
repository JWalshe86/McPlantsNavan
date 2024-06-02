from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_plants, name="plants"),
    path("add/", views.add_plant, name="add_plant"),
    path("<int:plant_id>/", views.plant_detail, name="plant_detail"),
    path("edit/<int:plant_id>/", views.edit_plant, name="edit_plant"),
]
