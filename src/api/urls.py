from django.urls import path
from . import views

urlpatterns = [
    path("categories", views.get_categories, name="get_categories"),
    path("images", views.get_images, name="get_images"),
]
