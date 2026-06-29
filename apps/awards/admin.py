"""
Admin configuration for awards app.
"""

from django.contrib import admin
from django.utils.html import format_html

from .models import Award


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    """
    Award admin with image preview.
    """

    list_display = [
        "title",
        "organization",
        "year",
        "display_order",
        "is_active",
    ]
    list_filter = [
        "is_active",
        "year",
    ]
    search_fields = [
        "title",
        "organization",
        "description",
    ]
    list_editable = [
        "display_order",
        "is_active",
    ]
    readonly_fields = [
        "created_at",
        "updated_at",
        "image_preview",
    ]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "doctor",
                    "title",
                    "organization",
                    "year",
                    "is_active",
                    "display_order",
                ),
            },
        ),
        (
            "Details",
            {
                "fields": (
                    "description",
                    "image",
                    "image_preview",
                ),
            },
        ),
        (
            "Dates",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px;" />',
                obj.image.url,
            )
        return "No image"
    image_preview.short_description = "Image Preview"
