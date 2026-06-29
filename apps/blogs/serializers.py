"""
Serializers for blogs app.
"""

from rest_framework import serializers

from .models import Blog


class BlogListSerializer(serializers.ModelSerializer):
    """
    Serializer for blog listing (lightweight).
    """

    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "slug",
            "featured_image",
            "excerpt",
            "published_at",
            "meta_title",
            "meta_description",
        ]
        read_only_fields = ["id", "slug", "published_at"]


class BlogDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for full blog detail.
    """

    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "slug",
            "featured_image",
            "excerpt",
            "content",
            "published_at",
            "meta_title",
            "meta_description",
            "meta_keywords",
        ]
        read_only_fields = ["id", "slug", "published_at"]
