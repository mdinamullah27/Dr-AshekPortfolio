"""
Common utilities.
"""

from django.utils.text import slugify


def generate_unique_slug(instance, value, slug_field="slug"):
    """
    Generate a unique slug for a model instance.
    """
    slug = slugify(value)
    original_slug = slug
    counter = 1

    model_class = instance.__class__
    while model_class.objects.filter(**{slug_field: slug}).exclude(pk=instance.pk).exists():
        slug = f"{original_slug}-{counter}"
        counter += 1

    return slug
