"""
    imports  -------------------------------------------------------
"""
# third party imports
from django.test import TestCase
from django.contrib.auth.models import User
# internal imports
from products.models import Product, Category


class TestManagementView(TestCase):

    def setUp(self):
        """
        Create test user, category, product and review
        """
        test_user = User.objects.create_user(username='test_user',
                                             password='test_password')

        User.objects.create_superuser(username='test_super_user',
                                      password='test_password')

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

    def test_get_newsletter_page(self):
        """
            This test checks that the newsletter list page
            is displayed correctly
            """
        self.client.login(username='test_super_user', password='testpassword')
        response = self.client.get('/newsletter/subscribers_list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsletter/newsletter_list.html')
