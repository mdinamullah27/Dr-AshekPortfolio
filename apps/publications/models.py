"""
Publication model for research papers, journals, and PDFs.
"""

from django.db import models

from apps.common.models import BaseModel


class Publication(BaseModel):
    """
    Research paper, journal article, or document.
    """

    PUBLICATION_TYPE_CHOICES = [
        ("journal", "Journal Article"),
        ("conference", "Conference Paper"),
        ("book_chapter", "Book Chapter"),
        ("thesis", "Thesis"),
        ("other", "Other"),
    ]

    doctor = models.ForeignKey(
        "doctor.DoctorProfile",
        on_delete=models.CASCADE,
        related_name="publications",
    )
    title = models.CharField(max_length=500)
    authors = models.CharField(
        max_length=500,
        blank=True,
        help_text="Comma-separated list of authors",
    )
    journal_name = models.CharField(
        max_length=255,
        blank=True,
        help_text="Journal or conference name",
    )
    publication_type = models.CharField(
        max_length=20,
        choices=PUBLICATION_TYPE_CHOICES,
        default="journal",
    )
    publication_date = models.DateField(blank=True, null=True)
    abstract = models.TextField(blank=True)
    doi = models.URLField(
        blank=True,
        verbose_name="DOI URL",
        help_text="Digital Object Identifier link",
    )
    pdf_file = models.FileField(
        upload_to="publications/pdfs/",
        blank=True,
        null=True,
        help_text="Upload PDF of the publication",
    )
    external_url = models.URLField(
        blank=True,
        help_text="Link to external publication page",
    )
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Publication"
        verbose_name_plural = "Publications"
        ordering = ["display_order", "-publication_date"]

    def __str__(self):
        return self.title
