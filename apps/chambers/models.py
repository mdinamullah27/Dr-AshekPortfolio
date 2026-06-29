"""
Chamber model for doctor's practice locations.
"""

from django.db import models

from apps.common.models import BaseModel


class Chamber(BaseModel):
    """
    A chamber/hospital where the doctor practices.
    """

    doctor = models.ForeignKey(
        "doctor.DoctorProfile",
        on_delete=models.CASCADE,
        related_name="chambers",
    )
    hospital_name = models.CharField(max_length=255)
    address = models.TextField()
    visiting_hours = models.CharField(
        max_length=255,
        blank=True,
        help_text="e.g., Sat-Sun: 10AM-2PM",
    )
    phone = models.CharField(max_length=20, blank=True)
    serial_booking_number = models.CharField(
        max_length=50,
        blank=True,
        help_text="Phone number for booking appointments",
    )
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Chamber"
        verbose_name_plural = "Chambers"
        ordering = ["display_order", "-created_at"]

    def __str__(self):
        return f"{self.hospital_name}"
