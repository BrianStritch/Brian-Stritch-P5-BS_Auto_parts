# Imports
# 3rd party:
from django.contrib.auth.models import User
from django.test import TestCase

# Internal:
from products.models import Category, Product, Manufacturer


class TestProductModels(TestCase):
    """
    A class for testing product models
    """

    def setUp(self):
        """
        Create test user, category, product and review
        """
        test_user = User.objects.create_user(username='test_user',
                                             password='test_password')

        Category.objects.create(name='test-category',
                                friendly_name='test category')

        Manufacturer.objects.create(name='test-manufacturer',
                                    friendly_name='test manufacturer')

        Product.objects.create(
            stock_no='test_stock_no',
            name='Test Name',
            price='99.99',
            description='Test Description',
            suits='universal',
            stock_qty='1',
            on_sale='True',
            has_sizes='False',
            rating='4.8',
            image_url='test_url',
            image='test_image.jpg',
        )

    def tearDown(self):
        """
        Delete test user, category, product and review
        """
        User.objects.all().delete()
        Category.objects.all().delete()
        Product.objects.all().delete()

    def testCreateproduct(self):
        """
        This test tests the creation of Product and verifies
        """
        user = User.objects.get(id=1)
        product = Product.objects.create(
            stock_no='test_stock_no 2',
            name='Test Name',
            price='99.99',
            description='Test Description',
            suits='universal',
            stock_qty='1',
            on_sale='True',
            has_sizes='False',
            rating='4.8',
            image_url='test_url',
            image='test_image.jpg',
        )
        product.save()
        self.assertTrue(product.save)

    def testCreatecategory(self):
        """
        This test tests the creation of categories and verifies
        """
        user = User.objects.get(id=1)
        category = Category.objects.create(name='test-category 2',
                                           friendly_name='test category 2')
        category.save()
        self.assertTrue(category.save)

    def testCreatemanufacturer(self):
        """
        This test tests the creation of manufacturer and verifies
        """
        user = User.objects.get(id=1)
        manufacturer = Manufacturer.objects.create(
            name='test-manufacturer 2', friendly_name='test manufacturer 2')
        manufacturer.save()
        self.assertTrue(manufacturer.save)

    def test_category_str_method(self):
        """
        This test tests the categories str method and verifies
        """
        category = Category.objects.get(name='test-category')
        self.assertEqual((category.__str__()), category.name)
        self.assertEqual(category.get_friendly_name(), category.friendly_name)

    def test_product_str_method(self):
        """
        This test tests the products str method and verifies
        """
        product = Product.objects.get(stock_no='test_stock_no')
        self.assertEqual((product.__str__()), product.name)

    def test_Category_str_method(self):
        """
        This test tests the category str method and verifies
        """
        category = Category.objects.get(name='test-category')
        self.assertEqual((category.__str__()), category.name)

    def test_Manufacturer_str_method(self):
        """
        This test tests the manufacturers str method and verifies
        """
        manufacturer = Manufacturer.objects.get(name='test-manufacturer')
        self.assertEqual((manufacturer.__str__()), manufacturer.name)
