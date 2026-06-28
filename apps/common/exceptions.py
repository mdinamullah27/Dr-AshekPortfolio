"""
Global exception handling.
"""

import logging

from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework import exceptions, status
from rest_framework.response import Response
from rest_framework.views import exception_handler

logger = logging.getLogger("apps")


def custom_exception_handler(exc, context):
    """
    Custom exception handler for consistent error responses.
    """
    response = exception_handler(exc, context)

    if response is not None:
        error_data = {
            "error": {
                "status_code": response.status_code,
                "message": _get_error_message(exc),
                "details": response.data,
            }
        }
        response.data = error_data
    else:
        logger.exception(f"Unhandled exception: {exc}")
        response = Response(
            {
                "error": {
                    "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "An internal server error occurred.",
                    "details": {},
                }
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return response


def _get_error_message(exc):
    """
    Extract error message from exception.
    """
    if isinstance(exc, exceptions.ValidationError):
        return "Validation error."
    elif isinstance(exc, exceptions.NotFound):
        return "Resource not found."
    elif isinstance(exc, exceptions.PermissionDenied):
        return "You do not have permission to perform this action."
    elif isinstance(exc, exceptions.NotAuthenticated):
        return "Authentication credentials were not provided."
    elif isinstance(exc, exceptions.AuthenticationFailed):
        return "Authentication failed."
    elif isinstance(exc, exceptions.Throttled):
        return "Request was throttled."
    elif isinstance(exc, Http404):
        return "Resource not found."
    elif isinstance(exc, PermissionDenied):
        return "You do not have permission to perform this action."
    else:
        return "An error occurred."
