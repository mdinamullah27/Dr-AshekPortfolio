"""
Admin configuration for publications app.
"""

from django.contrib import admin

from .models import Publication


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    """
    Publication admin with search and filtering.
    """

    list_display = [
        "title",
        "authors",
        "journal_name",
        "publication_type",
        "publication_date",
        "display_order",
        "is_active",
    ]
    list_filter = [
        "is_active",
        "publication_type",
        "publication_date",
    ]
    search_fields = [
        "title",
        "authors",
        "journal_name",
        "abstract",
    ]
    list_editable = [
        "display_order",
        "is_active",
    ]
    readonly_fields = [
        "created_at",
        "updated_at",
    ]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "doctor",
                    "title",
                    "authors",
                    "publication_type",
                    "is_active",
                    "display_order",
                ),
            },
        ),
        (
            "Publication Details",
            {
                "fields": (
                    "journal_name",
                    "publication_date",
                    "abstract",
                    "doi",
                    "external_url",
                    "pdf_file",
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
