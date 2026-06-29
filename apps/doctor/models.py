"""
Singleton DoctorProfile model.
"""

from django.db import models
from django.core.exceptions import ValidationError

from apps.common.models import BaseModel
from apps.common.utils import generate_unique_slug


class DoctorProfile(BaseModel):
    """
    Singleton model for Dr. Md. Ashek Ullah Khan's profile.
    Only one instance must exist at any time.
    """

    full_name = models.CharField(
        max_length=255,
        db_index=True,
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        db_index=True,
    )
    profile_image = models.ImageField(
        upload_to="doctor/profile/",
        blank=True,
        null=True,
    )
    cover_image = models.ImageField(
        upload_to="doctor/cover/",
        blank=True,
        null=True,
    )
    designation = models.CharField(
        max_length=255,
        blank=True,
        help_text="e.g., Consultant, Senior Consultant, Professor",
    )
    bmdc_number = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="BMDC Number",
        help_text="Bangladesh Medical and Dental Council registration number",
    )
    qualifications = models.TextField(
        blank=True,
        help_text="List of degrees and certifications",
    )
    current_position = models.CharField(
        max_length=255,
        blank=True,
        help_text="Current job title or position",
    )
    workplace = models.CharField(
        max_length=255,
        blank=True,
        help_text="Hospital or clinic name",
    )
    years_of_experience = models.PositiveIntegerField(default=0)
    surgeries_performed = models.PositiveIntegerField(default=0)
    short_biography = models.TextField(
        blank=True,
        help_text="Brief biography (2-3 paragraphs)",
    )
    full_biography_en = models.TextField(
        blank=True,
        verbose_name="Full Biography (English)",
    )
    full_biography_bn = models.TextField(
        blank=True,
        verbose_name="Full Biography (Bangla)",
    )

    # Social Links
    facebook_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)

    # SEO Fields
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
    canonical_url = models.URLField(
        blank=True,
        help_text="Canonical URL for SEO",
    )
    og_title = models.CharField(
        max_length=255,
        blank=True,
        help_text="Open Graph title",
    )
    og_description = models.TextField(
        blank=True,
        help_text="Open Graph description",
    )
    og_image = models.ImageField(
        upload_to="doctor/og/",
        blank=True,
        null=True,
        help_text="Open Graph image",
    )

    # System
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Doctor Profile"
        verbose_name_plural = "Doctor Profile"
        ordering = ["-created_at"]

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.full_name)
        if not self.pk and DoctorProfile.objects.exists():
            raise ValidationError("Only one DoctorProfile instance is allowed.")
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        """Return the singleton instance, creating one if it doesn't exist."""
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
