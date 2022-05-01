from django.test import TestCase

from django.test import TestCase
from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.models import User
from site_pages import urls, views
import unittest


class Test_user_profile_page_url(TestCase):

    """
        classmethod creating a user instance for testing
    """
    @classmethod
    def setUpTestData(cls):
        
        user = User.objects.create_user(
                id=1,
                email='test@test.com',
                username='test_username',
                password='testpassword',
                first_name='test_first',
                last_name='test_last'
            )
        user.save()      

    def test_sign_up_now_page_url(self):
        """
        This test checks that the sign up page
        is displayed
        """

        response = self.client.get('/sign_up/')
        self.assertTemplateUsed('nannys_alterantive/sign_up.html')
        self.assertEqual(response.status_code, 200)

    def test_get_profile_page(self):
        """
        This test checks that the profile page
        is displayed
        """
        user = User.objects.get(id=1)        
        self.client.login(username='test_username', password='testpassword')        
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nannys_alternative/profile.html', 'base.html')


    def test_edit_user_profile_page_url(self):

        """
        This test checks that the edit_profile page
        is displayed
        """
        
        user = User.objects.get(id=1)
        self.client.login(username='test_username', password='testpassword')

        response = self.client.get('/edit_profile/')
        self.assertTemplateUsed('nannys_alterantive/edit_profile.html')
        self.assertEqual(response.status_code, 200)

    # def test_get_edit_profile_page(self):
    #     """
    #     This test checks that the edit_profile page
    #     is displayed
    #     """
        
    #     user = User.objects.get(id=1)
    #     response = self.client.get('/edit_profile/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'nannys_alternative/edit_profile.html', 'base.html')

    def test_delete_profile_page_url(self):
        """
        This test checks that the delete_profile page
        is displayed
        """
        
        user = User.objects.get(id=1)
        self.client.login(username='test_username', password='testpassword')
        response = self.client.get('/delete_profile/1/')
        self.assertTemplateUsed('nannys_alterantive/delete_profile.html')
        self.assertEqual(response.status_code, 200)


class Test_additional_page_url(TestCase):

    def test_home_page_url(self):
        """
        This test checks that the home page
        is displayed
        """

        response = self.client.get('/')
        self.assertTemplateUsed('index.html')
        self.assertEqual(response.status_code, 200)

    def test_opening_hours_page_url(self):
        """
        This test checks that the opening hours page
        is displayed
        """

        response = self.client.get('/opening_hours/')
        
        self.assertTemplateUsed('nannys_alterantive/opening_hours.html')
        self.assertEqual(response.status_code, 200)

    def test_menu_page_url(self):
        """
        This test checks that the menu page
        is displayed
        """

        response = self.client.get('/menu/')
        self.assertTemplateUsed('nannys_alterantive/menu.html')
        self.assertEqual(response.status_code, 200)

    def test_about_page_url(self):
        """
        This test checks that the about page
        is displayed
        """

        response = self.client.get('/about/')
        self.assertTemplateUsed('nannys_alterantive/about.html')
        self.assertEqual(response.status_code, 200)