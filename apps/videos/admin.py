"""
Admin configuration for videos app.
"""

from django.contrib import admin
from django.utils.html import format_html

from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    """
    Video admin with thumbnail preview.
    """

    list_display = [
        "title",
        "video_type",
        "display_order",
        "is_active",
        "video_preview",
    ]
    list_filter = [
        "is_active",
        "video_type",
    ]
    search_fields = [
        "title",
        "description",
    ]
    list_editable = [
        "display_order",
        "is_active",
    ]
    readonly_fields = [
        "created_at",
        "updated_at",
        "video_preview",
    ]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "doctor",
                    "title",
                    "video_type",
                    "is_active",
                    "display_order",
                ),
            },
        ),
        (
            "Video Details",
            {
                "fields": (
                    "youtube_url",
                    "thumbnail",
                    "video_preview",
                    "description",
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

    def video_preview(self, obj):
        if obj.thumbnail:
            return format_html(
                '<img src="{}" style="max-height: 100px;" />',
                obj.thumbnail.url,
            )
        video_id = obj.youtube_video_id
        if video_id:
            return format_html(
                '<img src="https://img.youtube.com/vi/{}/mqdefault.jpg" style="max-height: 100px;" />',
                video_id,
            )
        return "No preview"
    video_preview.short_description = "Video Preview"
