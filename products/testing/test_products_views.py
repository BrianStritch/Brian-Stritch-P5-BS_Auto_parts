# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase

# Internal:
from products.models import Product, Manufacturer, Category
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestProductViews(TestCase):
    """
    A class for testing product views
    """
    def setUp(self):
        """
        Create test user(regular and super user), category and product
         """
        User.objects.create_user(
            username='test_user', password='test_password')

        User.objects.create_superuser(
            username='test_super_user', password='test_password')

        Category.objects.create(
            name='test-category', friendly_name='test category')

        Manufacturer.objects.create(
            name='test-manufacturer', friendly_name='test manufacturer')

        Product.objects.create(
            stock_no = 'test_stock_no',
            name='Test Name',
            price='99.99',
            description='Test Description', 
            suits = 'universal',
            stock_qty = '1',
            on_sale = 'True',
            has_sizes = 'False',            
            rating = '4.8',
            image_url = 'test_url',
            image = 'test_image.jpg',
        )

    def tearDown(self):
        """
        Delete test user, category, product
        """
        User.objects.all().delete()
        Category.objects.all().delete()
        Manufacturer.objects.all().delete()
        Product.objects.all().delete()

    def test_get_all_products(self):
        """
        This test tests get all products page and verifies
        """
        response = self.client.get('/products/', {'search_term': 'test',
                                                  'current_categories': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_search_all_products_no_query_string(self):
        """
        This test tests search all products with no query string
        """
        response = self.client.get('/products/', {'q': ''})
        self.assertRedirects(response, '/products/')

    def test_search_all_products_category_string(self):
        """
        This test tests search all product category string
        """
        response = self.client.get('/products/', {'category': 'air_filters'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_sort(self):
        """
        This test tests product sort with parameters
        """
        response = self.client.get('/products/', {'sort': 'name'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        response = self.client.get('/products/', {'sort': 'category'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        response = self.client.get('/products/', {'sort': 'category',
                                                  'direction': 'desc'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_product_detail(self):
        """
        This test tests get product details page and verifies
        """
        product = Product.objects.get()
        response = self.client.get(f'/products/{product.id}/',
                                   {'product': product})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_add_product_as_superuser(self):
        """
        This test tests add product page as a superuser and verifies
        """
        self.client.login(username='test_super_user', password='test_password')
        response = self.client.get('/products/add/')
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_add_product_as_non_superuser(self):
        """
        This test tests add product page as a non superuser and verifies
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get('/products/add/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         "Only staff have access to this feature.")

    def test_add_product_as_superuser_post(self):
        """
        This test tests add product page as a superuser and verifies
        """
        self.client.login(username='test_super_user', password='test_password')
        response = self.client.post('/products/add/', {
            'stock_no' : 'test_stock_no',
            'name':'Test Name',
            'price':'99.99',
            'description':'Test Description', 
            'suits' : 'universal',
            'stock_qty' : '1',
            'on_sale' : 'True',
            'has_sizes' : 'False',            
            'rating' : '4.8',
            'image_url' : 'test_url',
            'image' : 'test_image.jpg',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_get_edit_product_page(self):
        """
        This test tests edit product page(get) as a superuser and verifies
        """
        self.client.login(username='test_super_user', password='test_password')
        product = Product.objects.get()
        response = self.client.get(f'/products/edit/{product.id}/')
        self.assertTemplateUsed(response, 'products/edit_product.html')
 
    def test_get_edit_product_page_as_superuser(self):
        """
        This test checks that the edit_product page
        is displayed correctly
        """
        product = Product.objects.create(
            stock_no = 'test_stock_no',
            name='Test Name',
            price='99.99',
            description='Test Description', 
            suits = 'universal',
            stock_qty = '1',
            on_sale = 'True',
            has_sizes = 'False',            
            rating = '4.8',
            image_url = 'test_url',
            image = 'test_image.jpg',
        )
        product.save
        
        self.client.login(username='test_super_user', password='test_password')
        response = self.client.get(f'/products/edit/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')

   
    def test_edit_product_page_as_non_superuser(self):
        """
        This test tests edit product page as a non superuser and verifies
        """
        self.client.login(username='test_user', password='test_password')
        product = Product.objects.get()
        response = self.client.post(f'/products/edit/{product.id}/', {
            'name': 'Test Name Update',
            'price': '99.99',
            'colour': 'Test Colour Update',
            'code': '123456',
            'description': 'Test Description Update',
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Only staff have access to this feature.")

    def test_delete_product_as_superuser(self):
        """
        This test tests delete product as a superuser and verifies
        """
        self.client.login(username='test_super_user', password='test_password')
        product = Product.objects.get()
        response = self.client.post(f'/products/delete/{product.id}/')
        self.assertRedirects(response, '/products/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "You have successfully deleted your product.")
        deleted_product = Product.objects.filter(id=product.id)
        self.assertEqual(len(deleted_product), 0)

    def test_delete_product_as_non_superuser(self):
        """
        This test tests delete product as a non superuser and verifies
        """
        self.client.login(username='test_user', password='test_password')
        product = Product.objects.get()
        response = self.client.post(f'/products/delete/{product.id}/')
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Only staff have access to this feature.")



    def test_sale_item(self):
        """
        This test tests the sale item page and verifies
        """
        response = self.client.get('/products/', {'q': 'on_sale'})        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')