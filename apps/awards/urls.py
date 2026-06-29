"""
URL configuration for awards app.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = "awards"

router = DefaultRouter()
router.register("", views.AwardViewSet, basename="award")

urlpatterns = [
    path("", include(router.urls)),
]
