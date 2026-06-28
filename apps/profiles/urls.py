"""
URL configuration for profiles app.
"""

from django.urls import path

from . import views

app_name = "profiles"

urlpatterns = [
    # Public endpoints
    path(
        "",
        views.DoctorProfilePublicListView.as_view(),
        name="profile-list",
    ),
    path(
        "<slug:slug>/",
        views.DoctorProfilePublicDetailView.as_view(),
        name="profile-detail-slug",
    ),
    # Admin endpoints
    path(
        "admin/create/",
        views.DoctorProfileAdminCreateView.as_view(),
        name="profile-admin-create",
    ),
    path(
        "admin/<uuid:id>/",
        views.DoctorProfileAdminDetailView.as_view(),
        name="profile-admin-detail",
    ),
]
