from django.test import TestCase,Client
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import AccessKey
from accounts.models import CustomUser
from django.utils import timezone
from datetime import timedelta


class DashboardViewTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@example.com', password='12345')
        self.client.login(email='test@example.com', password='12345')
        self.access_key = AccessKey.objects.create(
            user=self.user, key='test_key', status='active',
            expiry_date = timezone.now() + timedelta(days=30)
        )

    def test_dashboard_view(self):
        url = reverse('dashboard')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test_key')

class AdminDashboardViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = CustomUser.objects.create_superuser(
            email='admin@example.com', password='12345'
        )
        self.client.login(email='admin@example.com', password='12345')
        self.access_key = AccessKey.objects.create(
            user=self.admin_user, key='admin_key', status='active',
            expiry_date = timezone.now() + timedelta(days=30)
        )

    def test_admin_dashboard_view(self):
        url = reverse('admin_dashboard')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'admin_key')


class AdminRevokeKeyViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = CustomUser.objects.create_superuser(
        email='admin@example.com', password='12345')
        self.client.login(email='admin@example.com', password='12345')
        self.access_key = AccessKey.objects.create(
            user=self.admin_user, key='test_key', status='active',
            expiry_date = timezone.now() + timedelta(days=30)
        )

    def test_admin_revoke_key_view(self):
        url = reverse('admin_revoke_key', args=[self.access_key.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Check for redirect after revoking
        self.access_key.refresh_from_db()
        self.assertEqual(self.access_key.status, 'revoked')


class GenerateKeyViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(email='admin@example.com', password='12345')
        self.client.login(email='admin@example.com', password='12345')

    def test_generate_key_view(self):
        url = reverse('generate_key')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test POST request to generate a key
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Check for redirect after key generation

        # Check if a key was actually created
        user_keys = AccessKey.objects.filter(user=self.user)
        self.assertTrue(user_keys.exists())

class KeyStatusApiTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            email='test@example.com', password='12345'
        )
        self.access_key = AccessKey.objects.create(
            user=self.user, key='test_key', status='active',
            expiry_date = timezone.now() + timedelta(days=30)
        )

    def test_key_status_api(self):
        url = reverse('key_status')
        response = self.client.get(url + '?email=test@example.com')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['key'], 'test_key')