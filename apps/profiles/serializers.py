"""
Serializers for profiles app.
"""

from rest_framework import serializers

from .models import DoctorProfile


class DoctorProfilePublicSerializer(serializers.ModelSerializer):
    """
    Serializer for public profile view (read-only, SEO-optimized).
    """

    class Meta:
        model = DoctorProfile
        fields = [
            "id",
            "full_name",
            "slug",
            "profile_image",
            "designation",
            "specialty",
            "sub_specialty",
            "years_of_experience",
            "biography",
            "primary_degree",
            "additional_qualifications",
            "current_workplace",
            "chamber_address",
            "consultation_time",
            "email",
            "phone",
            "appointment_url",
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
            "created_at",
        ]
        read_only_fields = ["id", "slug", "created_at"]


class DoctorProfileAdminSerializer(serializers.ModelSerializer):
    """
    Serializer for admin profile management (full CRUD).
    """

    class Meta:
        model = DoctorProfile
        fields = [
            "id",
            "user",
            "full_name",
            "slug",
            "profile_image",
            "designation",
            "specialty",
            "sub_specialty",
            "years_of_experience",
            "biography",
            "primary_degree",
            "additional_qualifications",
            "current_workplace",
            "chamber_address",
            "consultation_time",
            "email",
            "phone",
            "appointment_url",
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
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "slug", "created_at", "updated_at"]

    def validate_full_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Full name cannot be empty.")
        return value.strip()
