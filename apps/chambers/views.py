"""
Read-only views for chambers app.
"""

from rest_framework import viewsets

from .models import Chamber
from .serializers import ChamberSerializer


class ChamberViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public read-only endpoint for chambers.

    GET /api/v1/chambers/
    GET /api/v1/chambers/{id}/
    """

    serializer_class = ChamberSerializer
    queryset = Chamber.objects.filter(is_active=True)
    ordering_fields = ["display_order", "hospital_name"]
    ordering = ["display_order"]
