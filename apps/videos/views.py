"""
Read-only views for videos app.
"""

from rest_framework import viewsets

from .models import Video
from .serializers import VideoSerializer


class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public read-only endpoint for videos.

    GET /api/v1/videos/
    GET /api/v1/videos/{id}/
    """

    serializer_class = VideoSerializer
    queryset = Video.objects.filter(is_active=True)
    search_fields = ["title", "description"]
    filterset_fields = ["video_type"]
    ordering_fields = ["display_order", "title", "created_at"]
    ordering = ["display_order"]
