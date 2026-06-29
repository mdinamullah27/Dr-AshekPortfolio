"""
Serializers for videos app.
"""

from rest_framework import serializers

from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    """
    Read-only serializer for public video listing.
    """

    video_type_display = serializers.CharField(
        source="get_video_type_display",
        read_only=True,
    )
    embed_url = serializers.ReadOnlyField()

    class Meta:
        model = Video
        fields = [
            "id",
            "title",
            "description",
            "youtube_url",
            "thumbnail",
            "video_type",
            "video_type_display",
            "embed_url",
            "display_order",
        ]
        read_only_fields = ["id", "embed_url"]
