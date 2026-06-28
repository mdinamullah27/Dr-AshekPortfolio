"""
Settings package for drportfolio project.
Loads settings based on DJANGO_SETTINGS_MODULE environment variable.
"""

import os

environment = os.environ.get("DJANGO_SETTINGS_MODULE", "config.settings.development")

if "production" in environment:
    from .production import *  # noqa: F401, F403
elif "development" in environment:
    from .development import *  # noqa: F401, F403
else:
    from .base import *  # noqa: F401, F403
