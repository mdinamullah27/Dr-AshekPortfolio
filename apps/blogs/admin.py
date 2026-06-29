"""
Admin configuration for blogs app.
"""

from django.contrib import admin
from django.utils.html import format_html

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """
    Blog admin with rich text support and image preview.
    """

    list_display = [
        "title",
        "is_published",
        "published_at",
        "created_at",
        "updated_at",
    ]
    list_filter = [
        "is_published",
    ]
    search_fields = [
        "title",
        "excerpt",
        "content",
    ]
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = [
        "created_at",
        "updated_at",
        "featured_image_preview",
    ]
    list_editable = ["is_published"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "doctor",
                    "title",
                    "slug",
                    "is_published",
                    "published_at",
                ),
            },
        ),
        (
            "Content",
            {
                "fields": (
                    "featured_image",
                    "featured_image_preview",
                    "excerpt",
                    "content",
                ),
                "classes": ("wide",),
            },
        ),
        (
            "SEO",
            {
                "fields": (
                    "meta_title",
                    "meta_description",
                    "meta_keywords",
                ),
                "classes": ("collapse",),
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

    def featured_image_preview(self, obj):
        if obj.featured_image:
            return format_html(
                '<img src="{}" style="max-height: 150px; border-radius: 8px;" />',
                obj.featured_image.url,
            )
        return "No image"
    featured_image_preview.short_description = "Featured Image Preview"
