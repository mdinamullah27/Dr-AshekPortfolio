"""
API v1 URL configuration.
"""

from django.urls import include, path

urlpatterns = [
    # Authentication
    path("auth/", include("apps.accounts.urls")),
    # Doctor Profiles
    path("profiles/", include("apps.profiles.urls")),
]
