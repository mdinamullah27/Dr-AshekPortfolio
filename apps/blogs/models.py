"""
Blog model for SEO-optimized articles.
"""

from django.db import models
from django.utils import timezone

from apps.common.models import BaseModel
from apps.common.utils import generate_unique_slug


class Blog(BaseModel):
    """
    SEO-optimized blog post.
    """

    doctor = models.ForeignKey(
        "doctor.DoctorProfile",
        on_delete=models.CASCADE,
        related_name="blogs",
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        db_index=True,
    )
    featured_image = models.ImageField(
        upload_to="blogs/images/",
        blank=True,
        null=True,
    )
    excerpt = models.TextField(
        blank=True,
        help_text="Brief summary for previews and SEO",
    )
    content = models.TextField(
        help_text="Blog post content (supports HTML)",
    )
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)

    # SEO
    meta_title = models.CharField(
        max_length=255,
        blank=True,
        help_text="SEO meta title",
    )
    meta_description = models.TextField(
        blank=True,
        help_text="SEO meta description",
    )
    meta_keywords = models.CharField(
        max_length=500,
        blank=True,
        help_text="Comma-separated SEO keywords",
    )

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["-published_at", "-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.title)
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)
