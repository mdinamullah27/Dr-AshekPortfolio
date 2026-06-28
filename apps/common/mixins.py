"""
Reusable mixins for views.
"""


class CreateMessageMixin:
    """
    Mixin for creating instances with success message.
    """

    def perform_create(self, serializer):
        serializer.save()


class UpdateMessageMixin:
    """
    Mixin for updating instances with success message.
    """

    def perform_update(self, serializer):
        serializer.save()


class DestroyMessageMixin:
    """
    Mixin for deleting instances with success message.
    """

    def perform_destroy(self, instance):
        instance.delete()
