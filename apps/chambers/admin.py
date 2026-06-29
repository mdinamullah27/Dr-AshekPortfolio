"""
Admin configuration for chambers app.
"""

from django.contrib import admin

from .models import Chamber


@admin.register(Chamber)
class ChamberAdmin(admin.ModelAdmin):
    """
    Chamber admin configuration.
    """

    list_display = [
        "hospital_name",
        "address",
        "visiting_hours",
        "phone",
        "serial_booking_number",
        "display_order",
        "is_active",
    ]
    list_filter = [
        "is_active",
    ]
    search_fields = [
        "hospital_name",
        "address",
    ]
    list_editable = [
        "display_order",
        "is_active",
    ]
    readonly_fields = [
        "created_at",
        "updated_at",
    ]
    ordering = ["display_order", "-created_at"]
