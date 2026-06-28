"""
Custom permissions for profiles app.
"""

from rest_framework import permissions


class IsProfileOwnerOrAdmin(permissions.BasePermission):
    """
    Permission to only allow profile owners or admins.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user or request.user.is_staff
