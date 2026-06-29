"""
Serializers for awards app.
"""

from rest_framework import serializers

from .models import Award


class AwardSerializer(serializers.ModelSerializer):
    """
    Read-only serializer for public award listing.
    """

    class Meta:
        model = Award
        fields = [
            "id",
            "title",
            "organization",
            "year",
            "description",
            "image",
            "display_order",
        ]
        read_only_fields = ["id"]
