from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_plants, name="plants"),
    path("add/", views.add_plant, name="add_plant"),
    path("<int:plant_id>/", views.plant_detail, name="plant_detail"),
    path("edit/<int:plant_id>/", views.edit_plant, name="edit_plant"),
    path("delete/<int:plant_id>/", views.delete_plant, name="delete_plant"),
    path(
        "edit_event/<int:event_id>/",
        views.edit_event,
        name="edit_event"
    ),
    path(
        "delete_event/<int:event_id>/",
        views.delete_event,
        name="delete_event"
    ),
    path("all_events/", views.all_events, name="all_events"),
    path("add_event/", views.add_event, name="add_event"),
    path(
        "<int:event_id>/",
        views.event_detail,
        name="event_detail"
    ),
    path("all_reviews/", views.all_reviews, name="reviews"),
    path("add_review/", views.add_review, name="add_review"),
    path(
        "<int:review_id>/",
        views.review_detail,
        name="review_detail"
    ),
    path(
        "edit_review/<int:review_id>/",
        views.edit_review,
        name="edit_review"
    ),
    path(
        "delete_review/<int:review_id>/",
        views.delete_review,
        name="delete_review"
    ),
    path("stock_display/", views.stock_display, name="stock_display"),
]
