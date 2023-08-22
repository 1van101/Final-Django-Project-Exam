from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

UserModel = get_user_model()


class AppUserTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'test_user',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'gender': 'Male',
            'password': 'asdqwe!@#',
            'profile_picture': 'https://example.com/test_user.jpg',
            'is_visitor': False,
        }
        self.user = UserModel.objects.create_user(**self.user_data)

    def test_valid_username(self):
        self.user.username = 'john_doe'
        self.assertEqual(self.user.username, 'john_doe')

    def test_invalid_short_username_raises(self):
        with self.assertRaises(ValidationError) as context:
            self.user.username = 'j'
            self.user.full_clean()  # This should raise a validation error

        self.assertIn('Ensure username has at least 2 characters', str(context.exception))

    def test_valid_email(self):
        self.user.email = 'new_email@example.com'
        self.assertEqual(self.user.email, 'new_email@example.com')

    def test_invalid_email_raises(self):
        with self.assertRaises(ValidationError) as context:
            self.user.email = 'invalid_email'
            self.user.full_clean()  # This should raise a validation error

        self.assertIn('Enter a valid email address', str(context.exception))

    def test_full_name_property(self):
        self.assertEqual(self.user.full_name, 'Test User')

        self.user.first_name = 'John'
        self.user.last_name = ''
        self.assertEqual(self.user.full_name, 'John')

        self.user.first_name = ''
        self.user.last_name = 'Doe'
        self.assertEqual(self.user.full_name, 'Doe')

        self.user.first_name = ''
        self.user.last_name = ''
        self.assertEqual(self.user.full_name, 'test_user')