from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_plants, name="plants"),
    path("all_reviews", views.all_reviews, name="reviews"),
    path("add/", views.add_plant, name="add_plant"),
    path("add_review/", views.add_review, name="add_review"),
    path("edit_review/<int:review_id>/", views.edit_review, name="edit_review"),
    path("delete/<int:review_id>/", views.delete_review, name="delete_review"),
    path("<int:review_id>/", views.review_detail, name="review_detail"),
    path("<int:plant_id>/", views.plant_detail, name="plant_detail"),
    path("edit/<int:plant_id>/", views.edit_plant, name="edit_plant"),
    path("delete/<int:plant_id>/", views.delete_plant, name="delete_plant"),
]
