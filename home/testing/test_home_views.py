# imports
# 3rd party imports from django
from django.test import TestCase


class TestHomeViews(TestCase):
    """
    A class for testing home views
    """
    def test_get_home_page(self):
        """
        This test checks that the home landing page
        is displayed
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
    
    def test_get_shop_index_page(self):
        """
        This test checks that the shop index page
        is displayed
        """
        response = self.client.get('/shop/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/shop.html')