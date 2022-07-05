
# imports
# 3rd party imports from django
from django.test import TestCase
from django.contrib.messages import get_messages
from django.conf import settings
from django.contrib.auth.models import User

# internal imports from BS_Auto_parts
from checkout.models import Order
from profiles.models import UserProfile
from BS_Auto_Parts import urls
from checkout import urls


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

        order = Order.objects.create(
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

    def test_get_checkout_page(self):
        """
        This test checks the functionality of the checkout page response
        and redirection to the checkout success page
        """        
        response = self.client.post('/checkout/', {            
            'full_name':'Test User 2',
            'email':'test_email@gmail.com',
            'phone_number':'123456789',
            'country':'IE',
            'county': 'county',
            'town_or_city':'Test City',
            'street_address1':'Test Address 1',
            'street_address2':'Test Address 2',            
            'postcode':'postcode',
            'client_secret': '23456789',
            'stripe_public_key': 'public_key',
            'stripe_secret_key': 'secret_key',
        })
        order = Order.objects.get(full_name='Test User 2')
        o_n = order.order_number
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,f'/checkout/checkout_success/{o_n}')
    
    

        
        