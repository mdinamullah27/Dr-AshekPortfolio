"""
Read-only views for doctor app.
"""

from rest_framework import generics

from .models import DoctorProfile
from .serializers import DoctorProfileSerializer


class DoctorProfileView(generics.RetrieveAPIView):
    """
    Public endpoint to retrieve the doctor profile.

    GET /api/v1/doctor/
    """

    serializer_class = DoctorProfileSerializer
    queryset = DoctorProfile.objects.filter(is_active=True)

    def get_object(self):
        return self.queryset.first()
