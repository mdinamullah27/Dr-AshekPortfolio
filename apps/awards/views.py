"""
Read-only views for awards app.
"""

from rest_framework import viewsets

from .models import Award
from .serializers import AwardSerializer


class AwardViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public read-only endpoint for awards.

    GET /api/v1/awards/
    GET /api/v1/awards/{id}/
    """

    serializer_class = AwardSerializer
    queryset = Award.objects.filter(is_active=True)
    search_fields = ["title", "organization", "description"]
    ordering_fields = ["display_order", "year", "title"]
    ordering = ["display_order"]
