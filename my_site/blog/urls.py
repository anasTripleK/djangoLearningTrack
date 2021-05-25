from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page,name="starting-page"),
    path('posts/', views.all_posts, name="posts-page"),
    path('posts/<slug:slug>', views.each_post_detail, name="post-detail-page")
]
