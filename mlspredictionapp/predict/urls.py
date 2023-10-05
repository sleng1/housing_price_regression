from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("saved", views.saved, name="saved")
]