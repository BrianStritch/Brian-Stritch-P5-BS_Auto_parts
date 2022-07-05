# imports
# 3rd party imports from django
from decimal import Decimal
from django.test import TestCase

# internal imports from BS_Auto_parts
from products.models import Product, Category, Manufacturer
from BS_Auto_Parts import settings
from checkout.models import Order
from checkout.models import OrderLineItem


class TestCheckoutModels(TestCase):
    """
    A class for testing checkout models
    """
    def setUp(self):
        """
        Create a test product and order
        """
        Product.objects.create(            
          stock_no = "test-stock-no",
          name = "test name",
          description = "test description",
          price = '449.95',
          suits = "universal",
          stock_qty = 1,
          on_sale =  "False",
          has_sizes = "False",
          rating = '4.6',
          image_url = "testfile.jpg",
          image = "testfile.JPG"            
        )

        Order.objects.create(
            full_name='Test Name',
            email='test@gmail.com',
            phone_number='123456789',
            country='IE',
            town_or_city='Test City',
            street_address1='Test Address',
        )

    def tearDown(self):
        """
        Delete test products and orders
        """
        Product.objects.all().delete()
        Order.objects.all().delete()

    def test_order_str_method(self):
        """
        This test tests the order number string
        """
        order = Order.objects.get(email='test@gmail.com')
        self.assertEqual(str(order), order.order_number)