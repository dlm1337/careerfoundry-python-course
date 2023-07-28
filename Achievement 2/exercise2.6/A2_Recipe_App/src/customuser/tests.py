from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import CustomUser


class CustomUserModelTestCase(TestCase):
    def setUpTestData():
        CustomUser.objects.create(
            username="fakeuser",
            password="fakepassword",
            email="fakeEmail@fake.com",
        )

    def test_user_email(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field("email").verbose_name
        self.assertEqual(field_label, "email")

    def test_user_creation(self):
        user = CustomUser.objects.create(
            username="testuser", password="testpassword", email="test@example.com"
        )
        self.assertIsNotNone(user.id)
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.password, "testpassword")
        self.assertEqual(user.email, "test@example.com")

    def test_unique_username(self):
        CustomUser.objects.create(
            username="testuser", password="password1", email="email1@example.com"
        )
        with self.assertRaises(Exception):
            CustomUser.objects.create(
                username="testuser", password="password2", email="email2@example.com"
            )

    def test_unique_email(self):
        CustomUser.objects.create(
            username="username1", password="password1", email="test@example.com"
        )
        with self.assertRaises(Exception):
            CustomUser.objects.create(
                username="username2", password="password2", email="test@example.com"
            )

    def test_string_representation(self):
        user = CustomUser.objects.create(
            username="testuser", password="testpassword", email="test@example.com"
        )
        self.assertEqual(str(user), "testuser")

    def test_maximum_username_length(self):
        long_username = "a" * 151
        with self.assertRaises(ValidationError):
            user = CustomUser(
                username=long_username,
                password="testpassword",
                email="test@example.com",
            )
            user.full_clean()

    def test_maximum_password_length(self):
        long_password = "a" * 129
        with self.assertRaises(ValidationError):
            user = CustomUser(
                username="testuser", password=long_password, email="test@example.com"
            )
            user.full_clean()

    def test_valid_email_address(self):
        invalid_email = "invalid-email"
        with self.assertRaises(ValidationError):
            user = CustomUser(
                username="testuser", password="testpassword", email=invalid_email
            )
            user.full_clean()
