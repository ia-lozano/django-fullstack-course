from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # /models_app
    path("", views.index, name = "index"),
]