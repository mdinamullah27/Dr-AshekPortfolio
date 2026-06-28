"""
Models for profiles app.
"""

from django.conf import settings
from django.db import models

from apps.common.models import BaseModel
from apps.common.utils import generate_unique_slug


class DoctorProfile(BaseModel):
    """
    Doctor profile model with professional, academic, work, contact, social, and SEO fields.
    """

    # Basic Information
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="doctor_profile",
    )
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
        upload_to="profiles/images/",
        blank=True,
        null=True,
    )

    # Professional Information
    designation = models.CharField(
        max_length=255,
        blank=True,
        help_text="e.g., Consultant, Senior Consultant, Professor",
    )
    specialty = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
        help_text="e.g., Cardiology, Neurology, Orthopedics",
    )
    sub_specialty = models.CharField(
        max_length=255,
        blank=True,
        help_text="e.g., Interventional Cardiology",
    )
    years_of_experience = models.PositiveIntegerField(default=0)
    biography = models.TextField(blank=True)

    # Academic Information
    primary_degree = models.CharField(
        max_length=255,
        blank=True,
        help_text="e.g., MBBS, MD, PhD",
    )
    additional_qualifications = models.TextField(
        blank=True,
        help_text="Additional degrees, certifications, fellowships",
    )

    # Work Information
    current_workplace = models.CharField(
        max_length=255,
        blank=True,
        help_text="Hospital or clinic name",
    )
    chamber_address = models.TextField(blank=True)
    consultation_time = models.CharField(
        max_length=255,
        blank=True,
        help_text="e.g., Sat-Sun: 10AM-2PM",
    )

    # Contact Information
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    appointment_url = models.URLField(
        blank=True,
        help_text="Online appointment booking URL",
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
        upload_to="profiles/og/",
        blank=True,
        null=True,
        help_text="Open Graph image",
    )

    # System Fields
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "doctor profile"
        verbose_name_plural = "doctor profiles"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} - {self.specialty}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self, self.full_name)
        super().save(*args, **kwargs)
