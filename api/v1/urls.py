"""
API v1 URL configuration.
"""

from django.urls import include, path

urlpatterns = [
    path("doctor/", include("apps.doctor.urls")),
    path("chambers/", include("apps.chambers.urls")),
    path("blogs/", include("apps.blogs.urls")),
    path("publications/", include("apps.publications.urls")),
    path("videos/", include("apps.videos.urls")),
    path("awards/", include("apps.awards.urls")),
]
