"""
URL configuration for blogs app.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = "blogs"

router = DefaultRouter()
router.register("", views.BlogViewSet, basename="blog")

urlpatterns = [
    path("", include(router.urls)),
]
