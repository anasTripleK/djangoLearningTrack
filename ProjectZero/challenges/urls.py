from django.urls import path
# dot(.) means to navigate same folder
from . import views

urlpatterns = [
    path("january", views.index),
    path("february", views.february),
]
