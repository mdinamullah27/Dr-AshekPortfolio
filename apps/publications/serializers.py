"""
Serializers for publications app.
"""

from rest_framework import serializers

from .models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    """
    Read-only serializer for public publication listing.
    """

    publication_type_display = serializers.CharField(
        source="get_publication_type_display",
        read_only=True,
    )

    class Meta:
        model = Publication
        fields = [
            "id",
            "title",
            "authors",
            "journal_name",
            "publication_type",
            "publication_type_display",
            "publication_date",
            "abstract",
            "doi",
            "pdf_file",
            "external_url",
            "display_order",
        ]
        read_only_fields = ["id"]
