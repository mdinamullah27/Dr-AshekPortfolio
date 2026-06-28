"""
Business logic for profiles app.
"""

from .models import DoctorProfile


def get_active_profiles():
    """
    Get all active doctor profiles.
    """
    return DoctorProfile.objects.filter(is_active=True)


def get_profile_by_slug(slug):
    """
    Get a doctor profile by slug.
    """
    try:
        return DoctorProfile.objects.get(slug=slug, is_active=True)
    except DoctorProfile.DoesNotExist:
        return None


def get_profile_by_id(profile_id):
    """
    Get a doctor profile by ID.
    """
    try:
        return DoctorProfile.objects.get(id=profile_id)
    except DoctorProfile.DoesNotExist:
        return None


def create_profile(user, **kwargs):
    """
    Create a new doctor profile.
    """
    return DoctorProfile.objects.create(user=user, **kwargs)


def update_profile(profile, **kwargs):
    """
    Update doctor profile fields.
    """
    for field, value in kwargs.items():
        setattr(profile, field, value)
    profile.save()
    return profile


def delete_profile(profile):
    """
    Delete a doctor profile.
    """
    profile.delete()
