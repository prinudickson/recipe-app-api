"""
Tests for Models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """
    Tests Models

    Parameters
    ----------
    TestCase : _type_
        Tests of all model creations are listed here as different methods
    """

    def test_create_user_with_email_succesful(self):
        """
        test creation of user with email succesful
        """
        email = 'test@example.com'
        password = 'test1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
