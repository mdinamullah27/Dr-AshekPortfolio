"""
Serializers for chambers app.
"""

from rest_framework import serializers

from .models import Chamber


class ChamberSerializer(serializers.ModelSerializer):
    """
    Read-only serializer for public chamber listing.
    """

    class Meta:
        model = Chamber
        fields = [
            "id",
            "hospital_name",
            "address",
            "visiting_hours",
            "phone",
            "serial_booking_number",
            "display_order",
        ]
        read_only_fields = ["id"]
