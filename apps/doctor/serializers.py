"""
Serializers for doctor app.
"""

from rest_framework import serializers

from .models import DoctorProfile


class DoctorProfileSerializer(serializers.ModelSerializer):
    """
    Read-only serializer for public doctor profile.
    """

    class Meta:
        model = DoctorProfile
        fields = [
            "id",
            "full_name",
            "slug",
            "profile_image",
            "cover_image",
            "designation",
            "bmdc_number",
            "qualifications",
            "current_position",
            "workplace",
            "years_of_experience",
            "surgeries_performed",
            "short_biography",
            "full_biography_en",
            "full_biography_bn",
            "facebook_url",
            "linkedin_url",
            "youtube_url",
            "meta_title",
            "meta_description",
            "meta_keywords",
            "canonical_url",
            "og_title",
            "og_description",
            "og_image",
            "updated_at",
        ]
        read_only_fields = ["id", "slug", "updated_at"]
