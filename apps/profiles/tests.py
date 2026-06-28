"""
Tests for profiles app.
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from .models import DoctorProfile

User = get_user_model()


class DoctorProfileModelTest(TestCase):
    """
    Tests for DoctorProfile model.
    """

    def setUp(self):
        self.user = User.objects.create_user(
            email="doctor@example.com",
            first_name="Doctor",
            last_name="Smith",
            password="testpass123",
        )

    def test_create_profile(self):
        """Test creating a doctor profile."""
        profile = DoctorProfile.objects.create(
            user=self.user,
            full_name="Dr. Smith",
            specialty="Cardiology",
        )
        self.assertEqual(profile.full_name, "Dr. Smith")
        self.assertEqual(profile.specialty, "Cardiology")
        self.assertTrue(profile.is_active)

    def test_profile_slug_generation(self):
        """Test automatic slug generation."""
        profile = DoctorProfile.objects.create(
            user=self.user,
            full_name="Dr. John Smith",
            specialty="Cardiology",
        )
        self.assertIsNotNone(profile.slug)
        self.assertIn("dr-john-smith", profile.slug)

    def test_profile_str(self):
        """Test profile string representation."""
        profile = DoctorProfile.objects.create(
            user=self.user,
            full_name="Dr. Smith",
            specialty="Cardiology",
        )
        self.assertEqual(str(profile), "Dr. Smith - Cardiology")


class DoctorProfileAPITest(APITestCase):
    """
    Tests for Doctor Profile API endpoints.
    """

    def setUp(self):
        self.user = User.objects.create_user(
            email="doctor@example.com",
            first_name="Doctor",
            last_name="Smith",
            password="testpass123",
        )
        self.profile = DoctorProfile.objects.create(
            user=self.user,
            full_name="Dr. Smith",
            specialty="Cardiology",
            is_active=True,
        )
        self.profiles_url = "/api/v1/profiles/"

    def test_list_profiles_public(self):
        """Test listing profiles as unauthenticated user."""
        response = self.client.get(self.profiles_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_profile_by_slug(self):
        """Test retrieving a profile by slug."""
        response = self.client.get(f"{self.profiles_url}{self.profile.slug}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"]["full_name"], "Dr. Smith")

    def test_create_profile_authenticated(self):
        """Test creating a profile as authenticated user."""
        self.client.force_authenticate(user=self.user)
        data = {
            "full_name": "Dr. New Doctor",
            "specialty": "Neurology",
        }
        response = self.client.post(self.profiles_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_profile_unauthenticated(self):
        """Test creating a profile without authentication."""
        data = {
            "full_name": "Dr. New Doctor",
            "specialty": "Neurology",
        }
        response = self.client.post(self.profiles_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_profile_owner(self):
        """Test updating a profile as owner."""
        self.client.force_authenticate(user=self.user)
        data = {"specialty": "Updated Specialty"}
        response = self.client.patch(
            f"{self.profiles_url}admin/{self.profile.id}/",
            data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_profile_owner(self):
        """Test deleting a profile as owner."""
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(
            f"{self.profiles_url}admin/{self.profile.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
