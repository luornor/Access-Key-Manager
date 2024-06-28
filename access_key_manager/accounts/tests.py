from django.test import TestCase, Client
from django.urls import resolve, reverse

from .models import CustomUser, EmailVerification
from .utils import generate_activation_code
from django.utils import timezone
from datetime import timedelta
from . import views

# get Requests
class UserViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.verify_url = reverse('verify')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.home_url = reverse('home')
        self.dashboard_url = reverse('dashboard')

        # Create a test user
        self.test_user = CustomUser.objects.create_user(
            email='testuser@example.com',
            password='password1234'  # Ensure the password is not too common
        )

    def test_index_view_get(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'key_manager/index.html')

    def test_signup_view_get(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')

    def test_code_verification_view_get(self):
        response = self.client.get(self.verify_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/verify_email.html')

    def test_login_view_get(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')


# Post Requests
class AccountAuthTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.verify_url = reverse('verify')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.home_url = reverse('home')
        self.dashboard_url = reverse('dashboard')

        # Create a test user
        self.test_user = CustomUser.objects.create_user(
            email='testuser@example.com',
            password='password1234'  # Ensure the password is not too common
        )

    def test_signup_view_post(self):
        response = self.client.post(self.signup_url, {
            'email': 'newuser@example.com',
            'password1': 'ComplexPass123!',  # Use a more complex password
            'password2': 'ComplexPass123!'   # Ensure the passwords match
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.verify_url)
        self.assertTrue(CustomUser.objects.filter(email='newuser@example.com').exists())

        # Ensure the email verification code is created for the new user
        new_user = CustomUser.objects.get(email='newuser@example.com')
        self.assertTrue(EmailVerification.objects.filter(user=new_user).exists())



    def test_code_verification_view_post(self):
        generated_code = generate_activation_code()
        EmailVerification.objects.create(
            user=self.test_user,
            code=generated_code,
            expiry_date=timezone.now() + timedelta(hours=24)
        )

        response = self.client.post(self.verify_url, {
            'input1': str(generated_code)[0],
            'input2': str(generated_code)[1],
            'input3': str(generated_code)[2],
            'input4': str(generated_code)[3],
            'input5': str(generated_code)[4],
            'input6': str(generated_code)[5],
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.login_url)
        self.assertTrue(CustomUser.objects.filter(email='testuser@example.com').exists())

    def test_login_view_post(self):
        response = self.client.post(self.login_url, {
            'email': 'testuser@example.com',
            'password': 'password1234'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.dashboard_url)

    def test_logout_view_post(self):
        self.client.login(email='testuser@example.com', password='password1234')
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertIn(self.home_url, response.url)
