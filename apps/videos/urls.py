"""
URL configuration for videos app.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = "videos"

router = DefaultRouter()
router.register("", views.VideoViewSet, basename="video")

urlpatterns = [
    path("", include(router.urls)),
]
