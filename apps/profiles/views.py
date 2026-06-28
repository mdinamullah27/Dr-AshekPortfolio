"""
Views for profiles app.
"""

from rest_framework import generics, permissions, status
from rest_framework.response import Response

from apps.common.permissions import IsAdminOrReadOnly

from .models import DoctorProfile
from .serializers import DoctorProfileAdminSerializer, DoctorProfilePublicSerializer
from .services import get_active_profiles, get_profile_by_slug


class DoctorProfilePublicListView(generics.ListAPIView):
    """
    Public endpoint to list all active doctor profiles.

    GET /api/v1/profiles/
    """

    serializer_class = DoctorProfilePublicSerializer
    permission_classes = [permissions.AllowAny]
    queryset = DoctorProfile.objects.filter(is_active=True)
    filterset_fields = ["specialty", "designation"]
    search_fields = ["full_name", "specialty", "biography"]
    ordering_fields = ["full_name", "specialty", "years_of_experience"]
    ordering = ["-created_at"]


class DoctorProfilePublicDetailView(generics.RetrieveAPIView):
    """
    Public endpoint to retrieve a doctor profile by slug.

    GET /api/v1/profiles/{slug}/
    """

    serializer_class = DoctorProfilePublicSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "slug"
    queryset = DoctorProfile.objects.filter(is_active=True)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            {
                "message": "Profile retrieved successfully.",
                "data": serializer.data,
            }
        )


class DoctorProfileAdminCreateView(generics.CreateAPIView):
    """
    Admin endpoint to create a doctor profile.

    POST /api/v1/profiles/
    """

    serializer_class = DoctorProfileAdminSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(
            {
                "message": "Profile created successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )


class DoctorProfileAdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Admin endpoint to retrieve, update, or delete a doctor profile.

    GET /api/v1/profiles/{id}/
    PUT /api/v1/profiles/{id}/
    PATCH /api/v1/profiles/{id}/
    DELETE /api/v1/profiles/{id}/
    """

    serializer_class = DoctorProfileAdminSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]
    queryset = DoctorProfile.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            {
                "message": "Profile retrieved successfully.",
                "data": serializer.data,
            }
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "Profile updated successfully.",
                "data": serializer.data,
            }
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(
            {"message": "Profile deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )
