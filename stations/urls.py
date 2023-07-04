from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("map/", views.map, name="map"),
    path("stats/", views.stats, name="stats"),
    path('update-stats/', views.update_stats_endpoint, name='update-stats'),
    ]
