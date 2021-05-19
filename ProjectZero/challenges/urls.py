from django.urls import path
# dot(.) means to navigate same folder
from . import views

urlpatterns = [
    path("<month>", views.monthly_views),
]
