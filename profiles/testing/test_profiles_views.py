""" imports for profiles test_profiles_views.py """
# Imports
# 3rd party:
from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User

# Internal:
from checkout.models import Order
from profiles.models import UserProfile


class TestProfileViews(TestCase):

    def setUp(self):
        """
         This setup creates a test user,
         test product and test order
         """
        testuser = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test_user@test.com')
        testuser.save()

        Order.objects.create(
            order_number='12345678',
            user_profile=UserProfile.objects.get(user=testuser),
            full_name='Test User',
            email='test_user@test.com',
            phone_number='12345678',
            country='Test Country',
            postcode='Test postcode',
            town_or_city='Test city',
            street_address1='Test address',
            county='Test country',
        )

    def tearDown(self):
        """
        Delete test user and order
        """
        User.objects.all().delete()
        Order.objects.all().delete()

    def test_get_profile_page(self):
        """
        This test logins a test user and
        accesses their profile page (get) and verifies
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_post_profile_page(self):
        """
        This test logins a test user and
        accesses their profile page (post) and verifies
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.post('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
