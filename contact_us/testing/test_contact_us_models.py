# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase

# Internal:
from contact_us.models import ExistingUsersContactDetails, SiteUsersContactDetails
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestContactUsViews(TestCase):
    """
    A class for testing contact us views
    """
    def setUp(self):
        """
        Create test user(regular and super user), ExistingUsersContactDetails
        and SiteUsersContactDetails
         """
        User.objects.create_user(
            username='test_user', password='test_password')

        User.objects.create_superuser(
            username='test_super_user', password='test_password')

        user = User.objects.get(username='test_user')

        ExistingUsersContactDetails.objects.create(
            user = user,
            message = 'test_message',
            
        )
        SiteUsersContactDetails.objects.create(
            email = 'test_email 2',
            message = 'test message 2'
        )

    def tearDown(self):
        """
        Delete test user, category, product
        """
        User.objects.all().delete()
        ExistingUsersContactDetails.objects.all().delete()
        SiteUsersContactDetails.objects.all().delete()

    def testCreateExistingContact(self):
        """
        This test tests the creation of categories and verifies
        """
        user = User.objects.get(id=1)
        contact = ExistingUsersContactDetails.objects.create(
            user=user, 
            message='test message 2'
        ) 
        contact.save()
        self.assertTrue(contact.save)
    
    def testCreateSiteUserContact(self):
        """
        This test tests the creation of categories and verifies
        """
        user = User.objects.get(id=1)
        contact = SiteUsersContactDetails.objects.create(
            email = 'test_email 3', 
            message='test message 3'
        ) 
        contact.save()
        self.assertTrue(contact.save)

    