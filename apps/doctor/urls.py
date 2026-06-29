"""
URL configuration for doctor app.
"""

from django.urls import path

from . import views

app_name = "doctor"

urlpatterns = [
    path(
        "",
        views.DoctorProfileView.as_view(),
        name="doctor-profile",
    ),
]
