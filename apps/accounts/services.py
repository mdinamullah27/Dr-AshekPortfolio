"""
Business logic for accounts app.
"""

from django.contrib.auth import get_user_model

User = get_user_model()


def create_user(email, first_name, last_name, password):
    """
    Create a new user.
    """
    user = User.objects.create_user(
        email=email,
        first_name=first_name,
        last_name=last_name,
        password=password,
    )
    return user


def get_user_by_email(email):
    """
    Get user by email address.
    """
    try:
        return User.objects.get(email=email)
    except User.DoesNotExist:
        return None


def update_user(user, **kwargs):
    """
    Update user fields.
    """
    for field, value in kwargs.items():
        setattr(user, field, value)
    user.save()
    return user
