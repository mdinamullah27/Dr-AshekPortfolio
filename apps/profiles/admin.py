"""
Admin configuration for profiles app.
"""

from django.contrib import admin

from .models import DoctorProfile


@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    """
    Doctor profile admin configuration.
    """

    list_display = [
        "full_name",
        "specialty",
        "designation",
        "current_workplace",
        "is_active",
        "created_at",
    ]
    list_filter = [
        "is_active",
        "specialty",
        "designation",
    ]
    search_fields = [
        "full_name",
        "specialty",
        "biography",
        "current_workplace",
    ]
    prepopulated_fields = {"slug": ("full_name",)}
    readonly_fields = [
        "created_at",
        "updated_at",
    ]
    list_editable = ["is_active"]
