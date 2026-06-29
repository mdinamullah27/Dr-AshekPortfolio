"""
Award model for doctor's achievements and recognition.
"""

from django.db import models

from apps.common.models import BaseModel


class Award(BaseModel):
    """
    An award, achievement, or recognition received by the doctor.
    """

    doctor = models.ForeignKey(
        "doctor.DoctorProfile",
        on_delete=models.CASCADE,
        related_name="awards",
    )
    title = models.CharField(max_length=255)
    organization = models.CharField(
        max_length=255,
        blank=True,
        help_text="Awarding organization or institution",
    )
    year = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="Year the award was received",
    )
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="awards/images/",
        blank=True,
        null=True,
    )
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Award"
        verbose_name_plural = "Awards"
        ordering = ["display_order", "-year"]

    def __str__(self):
        return self.title
