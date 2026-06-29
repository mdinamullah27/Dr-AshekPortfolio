"""
Chambers app configuration.
"""

from django.apps import AppConfig


class ChambersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.chambers"
    verbose_name = "Chambers"
