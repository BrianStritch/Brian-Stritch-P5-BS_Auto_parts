
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.messages import get_messages
from django.conf import settings
from django.contrib.auth.models import User

# Internal:
from checkout.models import Order
from profiles.models import UserProfile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestCheckoutViews(TestCase):
    """
    A class for testing checkout views
    """
    def setUp(self):
        """
        Create test users(standard and superuser) and a test order
        """
        testuser = User.objects.create_user(
            username='testuser', password='testpassword')
        test_user_superuser = User.objects.create_superuser(
            username='test_user_superuser', password='test_password')

        testuser.save()
        test_user_superuser.save()
        testuser = UserProfile.objects.get(user=testuser)

        Order.objects.create(
            full_name='Test User',
            email='test_email@gmail.com',
            phone_number='123456789',
            country='IE',
            town_or_city='Test City',
            street_address1='Test Address 1',
            street_address2='Test Address 2',
            user_profile=testuser
        )

    def tearDown(self):
        """
        Delete test orders
        """
        Order.objects.all().delete()

    def test_checkout_view_empty_cart(self):
        """
        This test test an empty cart for checkout and verifies
        """
        response = self.client.get('/checkout/')
        self.assertRedirects(response, '/products/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), "There's nothing in your bag at the moment")