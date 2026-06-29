"""
Read-only views for publications app.
"""

from rest_framework import viewsets

from .models import Publication
from .serializers import PublicationSerializer


class PublicationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public read-only endpoint for publications.

    GET /api/v1/publications/
    GET /api/v1/publications/{id}/
    """

    serializer_class = PublicationSerializer
    queryset = Publication.objects.filter(is_active=True)
    search_fields = ["title", "authors", "journal_name", "abstract"]
    filterset_fields = ["publication_type"]
    ordering_fields = ["publication_date", "display_order", "title"]
    ordering = ["-publication_date"]
