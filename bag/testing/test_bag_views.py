""" imports for test bag views .py """
# imports
# 3rd party imports from django
from django.contrib.messages import get_messages
from django.test import TestCase

# internal imports from BS_Auto_parts
from products.models import Product


class TestBagViews(TestCase):
    """
    A class for testing bag views
    """

    def setUp(self):
        """
        Create a test product
        """
        Product.objects.create(stock_no="test-stock-no",
                               name="test name",
                               description="test description",
                               price='449.95',
                               suits="universal",
                               stock_qty=1,
                               on_sale="False",
                               has_sizes="True",
                               rating='4.6',
                               image_url="testfile.jpg",
                               image="testfile.JPG")

    def tearDown(self):
        """
        Delete test products
        """
        Product.objects.all().delete()

    def test_get_bag_page(self):
        """
        This test checks that the bag page is displayed
        """
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_empty_bag_no_size(self):
        """
        This test adds a product with no size to an empty bag and verifies
        """
        product = Product.objects.get(stock_no="test-stock-no")
        response = self.client.post(f'/bag/add/{product.id}/', {
            "quantity": 1,
            "redirect_url": "view_bag"
        })
        bag = self.client.session['bag']
        self.assertEqual(bag[str(product.id)], 1)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'You have succesfully added "test name" to the shopping bag.'
        )  # noqa

    def test_add_to_empty_bag_with_size(self):
        """
        This test adds a product with a
        size to an empty bag and verifies
        """
        product = Product.objects.get(stock_no="test-stock-no")
        response = self.client.post(f'/bag/add/{product.id}/', {
            "quantity": 1,
            "redirect_url": "view_bag",
            "product_size": 1
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(
            messages[0]
        ), 'You have succesfully added "1" of our "test name" size "1" to the shopping bag.'
                         )  # noqa

    def test_adjust_bag_quantity_to_two(self):
        """
        This test updates a products quantity to 2 and verifies
        """
        product = Product.objects.get(stock_no="test-stock-no")
        response = self.client.post(f'/bag/edit/{product.id}/', {
            "quantity": 2,
            "redirect_url": "view_bag",
        })
        bag = self.client.session['bag']
        self.assertEqual(bag[str(product.id)], 2)
        messages = list(get_messages(response.wsgi_request))
        product_id = bag[str(product.id)]
        self.assertEqual(
            str(messages[0]),
            'You have succesfully edited the quantity of "test name" in your shopping bag.'  # noqa
        )

    def test_adjust_bag_quantity_to_zero(self):
        """
        This test reduces the bag from 1 item to 0 items and verifies
        """
        product = Product.objects.get(stock_no="test-stock-no")
        response = self.client.post(f'/bag/edit/{product.id}/', {
            'quantity': 1,
            "redirect_url": "view_bag",
        })
        self.assertRedirects(response, '/bag/')
        bag = self.client.session['bag']
        self.assertEqual(bag[str(product.id)], 1)
        response = self.client.post(f'/bag/edit/{product.id}/', {
            'quantity': 0,
            "redirect_url": "view_bag",
        })
        self.assertRedirects(response, '/bag/')
        bag = self.client.session['bag']
        self.assertEqual(bag, {})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'You have succesfully removed "test name" from your shopping bag.'
        )  # noqa

    def test_remove_product_from_bag(self):
        """
        This test removes a product from the bag and verifies
        """
        product = Product.objects.get(stock_no="test-stock-no")
        self.client.post(f'/bag/add/{product.id}/', {
            'quantity': 1,
            "redirect_url": "view_bag"
        })
        bag = self.client.session['bag']
        self.assertEqual(bag[str(product.id)], 1)
        response = self.client.post(f'/bag/delete/{product.id}/')
        bag = self.client.session['bag']
        self.assertEqual(bag, {})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[1]),
            'You have succesfully removed "test name" from your shopping bag.'
        )  # noqa

    def test_remove_product_from_bag_with_size(self):
        """
        This test removes a product \
            with a size from the bag and verifies
        """
        product = Product.objects.get(stock_no="test-stock-no")
        self.client.post(f'/bag/add/{product.id}/', {
            'quantity': 1,
            "redirect_url": "view_bag",
            "product_size": 1
        })
        response = self.client.post(f'/bag/delete/{product.id}/',
                                    {"product_size": 1})
        bag = self.client.session['bag']
        self.assertEqual(bag, {})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(
            messages[1]
        ), 'You have succesfully removed "test name" size "1" from your shopping bag.'
                         )  # noqa

    def test_remove_product_from_bag_exception(self):
        """
        This test tries to remove a product from a bag
        that doesnt exist, and an exception is thrown is verified
        """
        product = Product.objects.get(stock_no="test-stock-no")
        response = self.client.post(f'/bag/delete/{product.id}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual("list index out of range", "list index out of range")
