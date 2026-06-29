"""
URL configuration for chambers app.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = "chambers"

router = DefaultRouter()
router.register("", views.ChamberViewSet, basename="chamber")

urlpatterns = [
    path("", include(router.urls)),
]
