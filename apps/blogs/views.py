"""
Read-only views for blogs app.
"""

from rest_framework import viewsets

from .models import Blog
from .serializers import BlogDetailSerializer, BlogListSerializer


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Public read-only endpoint for blog posts.

    GET /api/v1/blogs/
    GET /api/v1/blogs/{slug}/
    """

    queryset = Blog.objects.filter(is_published=True)
    lookup_field = "slug"
    search_fields = ["title", "excerpt", "content"]
    ordering_fields = ["published_at", "title"]
    ordering = ["-published_at"]

    def get_serializer_class(self):
        if self.action == "list":
            return BlogListSerializer
        return BlogDetailSerializer
