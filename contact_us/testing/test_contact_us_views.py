# imports
# 3rd party imports from django
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase

# internal imports from BS_Auto_parts
from contact_us.models import ExistingUsersContactDetails, SiteUsersContactDetails


class TestProductViews(TestCase):
    """
    A class for testing product views
    """

    def setUp(self):
        """
        Create test user(regular and super user), category and product
         """
        User.objects.create_user(username='test_user',
                                 password='test_password')

        User.objects.create_superuser(username='test_super_user',
                                      password='test_password')

        user = User.objects.get(username='test_user')

        ExistingUsersContactDetails.objects.create(
            user=user,
            message='test_message',
        )
        SiteUsersContactDetails.objects.create(email='test_email 2',
                                               message='test message 2')

    def tearDown(self):
        """
        Delete test user, category, product
        """
        User.objects.all().delete()
        ExistingUsersContactDetails.objects.all().delete()

    def test_display_subscribers_list(self):
        """
        This test tests get all contact_us Queries page and verifies
        """
        response = self.client.get('/contact_us/', )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_us/contact_us.html')
