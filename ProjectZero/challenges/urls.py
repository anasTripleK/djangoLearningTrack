from django.urls import path
# dot(.) means to navigate same folder
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:month>", views.monthly_views_integer_override),
    path("<str:month>", views.monthly_views, name="monthsUrl"),
]
