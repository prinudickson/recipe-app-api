"""
Tests for Django admin
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """
    Tests for the Django Admin

    Parameters
    ----------
    TestCase : _type_
        _description_
    """
    def setUp(self):
        """
        Create user and Client

        Returns
        -------
        _type_
            _description_
        """
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='admin1234',
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='user1234',
            name='Test User'
        )

        #return super().setUp()

    def test_users_list(self):
        """
        Test that users are listed on page.
        """
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
