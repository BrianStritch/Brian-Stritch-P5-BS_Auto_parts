from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.db.models import Q
from django.views.generic import TemplateView, UpdateView, DeleteView
from django.views import generic, View
from products.models import Product, Category, Manufacturer
from contact_us.models import ExistingUsersContactDetails, SiteUsersContactDetails


class StoreManagement(TemplateView):
    def get(self, request):
        template_name = 'storeowners/management.html'
        context = {
           'stop_toast_cart': True,

        }
        return render(request, template_name, context)


class StockManagement(TemplateView):
    def get(self, request):
        products = Product.objects.all()
        template_name = 'storeowners/current_stock.html'
        context = {
           'stop_toast_cart': True,
           'products': products,

        }
        return render(request, template_name, context)

class QueryManagement(TemplateView):
    def get(self, request):
        existing_contacts = ExistingUsersContactDetails.objects.all()
        new_users = SiteUsersContactDetails.objects.all()
        template_name = 'storeowners/contact_us_list.html'
        context = {
           'stop_toast_cart': True,
           'existing_contacts': existing_contacts,
           'new_users': new_users,
        }
        return render(request, template_name, context)

        

class ToggleExistingContactUsStatus(TemplateView):
    """
        Class based view to toggle the liked status for
        the selected post and saving to the database.
    """
    def post(self, request, pk):
        """
        POST request for processing the Post liked status
        data passed from the reviews details page and if
        form is valid updates and saves status to database.
        """
        query = get_object_or_404(ExistingUsersContactDetails, pk=pk)        
        template_name = 'storeowners/contact_us_list.html'
        if query.status == 1:
            query.status = 0
            query.save()
            messages.success(request, 'You have succesfully edited the contact status for the selected query.')
        else:
            query.status = 1
            query.save()
            messages.success(request, 'You have completed liked this request.')

        return render(request, template_name)


class ToggleNewUserContactUsStatus(TemplateView):
    """
        Class based view to toggle the status for
        the selected post and saving to the database.
    """
    def post(self, request, pk):
        """
        POST request for processing the Post liked status
        data passed from the reviews details page and if
        form is valid updates and saves status to database.
        """
        query = get_object_or_404(SiteUsersContactDetails, pk=pk)
        template_name = 'storeowners/contact_us_list.html'    
        print('getting here')
        if query.status == 1:
            query.status = 0
            query.save()
            messages.success(request, 'You have succesfully edited the contact status for the selected query.')
        else:
            query.status = 1
            query.save()
            messages.success(request, 'You have completed liked this request.')

        return render(request, template_name)
