"""
Custom permissions for accounts app.
"""

from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Permission to only allow owners of an object.
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user
