"""
Video model for surgery and educational YouTube videos.
"""

from django.db import models

from apps.common.models import BaseModel


class Video(BaseModel):
    """
    YouTube video embed for surgery or educational content.
    """

    VIDEO_TYPE_CHOICES = [
        ("surgery", "Surgery"),
        ("educational", "Educational"),
        ("interview", "Interview"),
        ("other", "Other"),
    ]

    doctor = models.ForeignKey(
        "doctor.DoctorProfile",
        on_delete=models.CASCADE,
        related_name="videos",
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    youtube_url = models.URLField(
        help_text="Full YouTube video URL",
    )
    thumbnail = models.ImageField(
        upload_to="videos/thumbnails/",
        blank=True,
        null=True,
        help_text="Custom thumbnail (leave blank to use YouTube default)",
    )
    video_type = models.CharField(
        max_length=20,
        choices=VIDEO_TYPE_CHOICES,
        default="other",
    )
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
        ordering = ["display_order", "-created_at"]

    def __str__(self):
        return self.title

    @property
    def youtube_video_id(self):
        """Extract YouTube video ID from URL."""
        import re
        patterns = [
            r"(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([^&\s?]+)",
        ]
        for pattern in patterns:
            match = re.search(pattern, self.youtube_url)
            if match:
                return match.group(1)
        return None

    @property
    def embed_url(self):
        """Get YouTube embed URL."""
        video_id = self.youtube_video_id
        if video_id:
            return f"https://www.youtube.com/embed/{video_id}"
        return self.youtube_url
