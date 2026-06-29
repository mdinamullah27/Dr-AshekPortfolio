"""
Admin configuration for doctor app.
"""

from django.contrib import admin
from django.utils.html import format_html

from .models import DoctorProfile


@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    """
    Singleton DoctorProfile admin with full customization.
    """

    list_display = [
        "full_name",
        "designation",
        "workplace",
        "years_of_experience",
        "is_active",
        "updated_at",
    ]
    list_filter = [
        "is_active",
    ]
    search_fields = [
        "full_name",
        "designation",
        "workplace",
        "qualifications",
    ]
    readonly_fields = [
        "created_at",
        "updated_at",
        "profile_image_preview",
        "cover_image_preview",
        "og_image_preview",
    ]
    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "full_name",
                    "slug",
                    "profile_image",
                    "profile_image_preview",
                    "cover_image",
                    "cover_image_preview",
                ),
            },
        ),
        (
            "Professional Information",
            {
                "fields": (
                    "designation",
                    "bmdc_number",
                    "qualifications",
                    "current_position",
                    "workplace",
                    "years_of_experience",
                    "surgeries_performed",
                ),
            },
        ),
        (
            "Biography",
            {
                "fields": (
                    "short_biography",
                    "full_biography_en",
                    "full_biography_bn",
                ),
                "classes": ("wide",),
            },
        ),
        (
            "Social Links",
            {
                "fields": (
                    "facebook_url",
                    "linkedin_url",
                    "youtube_url",
                ),
            },
        ),
        (
            "SEO",
            {
                "fields": (
                    "meta_title",
                    "meta_description",
                    "meta_keywords",
                    "canonical_url",
                    "og_title",
                    "og_description",
                    "og_image",
                    "og_image_preview",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "System",
            {
                "fields": (
                    "is_active",
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )

    def has_add_permission(self, request):
        return not DoctorProfile.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def profile_image_preview(self, obj):
        if obj.profile_image:
            return format_html(
                '<img src="{}" style="max-height: 150px; border-radius: 8px;" />',
                obj.profile_image.url,
            )
        return "No image"
    profile_image_preview.short_description = "Profile Image Preview"

    def cover_image_preview(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" style="max-height: 150px; border-radius: 8px;" />',
                obj.cover_image.url,
            )
        return "No image"
    cover_image_preview.short_description = "Cover Image Preview"

    def og_image_preview(self, obj):
        if obj.og_image:
            return format_html(
                '<img src="{}" style="max-height: 100px;" />',
                obj.og_image.url,
            )
        return "No image"
    og_image_preview.short_description = "OG Image Preview"

    def save_model(self, request, obj, form, change):
        if not change and DoctorProfile.objects.exists():
            return
        super().save_model(request, obj, form, change)
