# imports
# 3rd party imports from django
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.db.models import Q
from django.views.generic import TemplateView, UpdateView, DeleteView
from django.views import generic, View
from django.contrib.auth.decorators import login_required


# internal imports from BS_Auto_parts
from products.models import Product, Category, Manufacturer
from products.forms import ManufacturerForm, CategoryForm, ProductForm
from contact_us.models import ExistingUsersContactDetails, SiteUsersContactDetails


class StoreManagement(TemplateView):

    def get(self, request):
        query = None
        sort = None
        direction = None
        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('checkout'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            product = Product.objects.all()
            products = product.filter(queries)

            current_sorting = f'{sort}_{direction}'
                    
            context = {
            'products': products,
            'search_term': query,
            'current_sorting': current_sorting,
            }
            return render(
                request, 'products/products.html', context)
        else:
            template_name = 'storeowners/management.html'
            context = {
            'stop_toast_cart': True,

            }
            return render(request, template_name, context)


class StockManagement(TemplateView):
    def get(self, request):
        query = None
        sort = None
        direction = None
        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('checkout'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            product = Product.objects.all()
            products = product.filter(queries)

            current_sorting = f'{sort}_{direction}'
                    
            context = {
            'products': products,
            'search_term': query,
            'current_sorting': current_sorting,
            }
            return render(
                request, 'products/products.html', context)
        else:
            products = Product.objects.all()
            template_name = 'storeowners/current_stock.html'
            context = {
            'stop_toast_cart': True,
            'products': products,

            }
            return render(request, template_name, context)


class QueryManagement(TemplateView):
    def get(self, request):
        query = None
        sort = None
        direction = None
        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('checkout'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            product = Product.objects.all()
            products = product.filter(queries)

            current_sorting = f'{sort}_{direction}'
                    
            context = {
            'products': products,
            'search_term': query,
            'current_sorting': current_sorting,
            }
            return render(
                request, 'products/products.html', context)
        else:
            existing_contacts = ExistingUsersContactDetails.objects.all().order_by('status')
            new_users = SiteUsersContactDetails.objects.all().order_by('status')
            template_name = 'storeowners/contact_us_list.html'
            context = {
            'stop_toast_cart': True,
            'existing_contacts': existing_contacts,
            'new_users': new_users,
            }
            return render(request, template_name, context)


class NewQueryDetails(TemplateView):
    def get(self, request, pk):
        query = None
        sort = None
        direction = None
        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('checkout'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            product = Product.objects.all()
            products = product.filter(queries)

            current_sorting = f'{sort}_{direction}'
                    
            context = {
            'products': products,
            'search_term': query,
            'current_sorting': current_sorting,
            }
            return render(
                request, 'products/products.html', context)
        else:
            user = get_object_or_404(SiteUsersContactDetails, pk=pk)
            template_name = 'storeowners/contact_message.html'
            context = {
            'stop_toast_cart': True,
            'user': user,
            }
            return render(request, template_name, context)


class ExistingQueryDetails(TemplateView):
    def get(self, request, pk):
        query = None
        sort = None
        direction = None
        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('checkout'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            product = Product.objects.all()
            products = product.filter(queries)

            current_sorting = f'{sort}_{direction}'
                    
            context = {
            'products': products,
            'search_term': query,
            'current_sorting': current_sorting,
            }
            return render(
                request, 'products/products.html', context)
        else:
            user = get_object_or_404(ExistingUsersContactDetails, pk=pk)
            template_name = 'storeowners/contact_message.html'
            context = {
            'stop_toast_cart': True,
            'user': user,
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
        existing_contacts = ExistingUsersContactDetails.objects.all().order_by('status')
        new_users = SiteUsersContactDetails.objects.all().order_by('status')        
        template_name = 'storeowners/contact_us_list.html'
        context = {
            'stop_toast_cart': True,
            'existing_contacts': existing_contacts,
            'new_users': new_users,
        }  
        if query.status == 1:
            query.status = 0
            query.save()
            messages.success(request, 'You have succesfully edited the contact status for the selected query.')
        else:
            query.status = 1
            query.save()
            messages.success(request, 'You have completed liked this request.')

        return render(request, template_name, context)


class ToggleNewUserContactUsStatus(View):
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
        existing_contacts = ExistingUsersContactDetails.objects.all()
        new_users = SiteUsersContactDetails.objects.all()
        template_name = 'storeowners/contact_us_list.html'
        context = {
            'stop_toast_cart': True,
            'existing_contacts': existing_contacts,
            'new_users': new_users,

        }    
        print('getting here')
        if query.status == 1:
            query.status = 0
            query.save()
            messages.success(request, 'You have succesfully edited the contact status for the selected query.')
        else:
            query.status = 1
            query.save()
            messages.success(request, 'You have completed liked this request.')

        return render(request, template_name, context)


class ManAndCatList(TemplateView):
    
    def get(self, request):
        query = None
        sort = None
        direction = None
        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('checkout'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            product = Product.objects.all()
            products = product.filter(queries)

            current_sorting = f'{sort}_{direction}'
                    
            context = {
            'products': products,
            'search_term': query,
            'current_sorting': current_sorting,
            }
            return render(
                request, 'products/products.html', context)
        else:
            manufacturers = Manufacturer.objects.all().order_by('name')
            categories = Category.objects.all().order_by('pk')
            template_name = 'storeowners/manufacturer_and_category_list.html'
            context = {
            'stop_toast_cart': True,
            'manufacturers': manufacturers,
            'categories': categories,
            }
        
            return render(request, template_name, context)

@login_required
def add_manufacturer(request):
    """ 
    Add a manufacturer to the store
    """
    query = None
    sort = None
    direction = None

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(
                request, "You didn't enter any search criteria!")
            return redirect(reverse('checkout'))

        queries = Q(
            name__icontains=query) | Q(description__icontains=query)
        product = Product.objects.all()
        products = product.filter(queries)

        current_sorting = f'{sort}_{direction}'
                
        context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting,
        }
        return render(
            request, 'products/products.html', context)
    else:
        if not request.user.is_superuser:
            messages.error(request, 'Only staff have access to this feature.')
            return redirect(reverse('stock_management'))

        if request.method == 'POST':
            form = ManufacturerForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your manufacturer has been succesfully added.')
                template_name = 'storeowners/manufacturer_and_category_list.html'
                manufacturers = Manufacturer.objects.all()
                categories = Category.objects.all()
                context = {
                    'manufacturers': manufacturers,
                    'categories': categories,
                    'stop_toast_cart': True,
                }
                return render(request, template_name, context)
                    
            else:
                messages.error(request, 'Failed to add manufacturer. Please check your form details.')
        else:
            form = ManufacturerForm()
            template = 'storeowners/add_manufacturer.html'
            context = {
                'form': form,
                'stop_toast_cart': True,
            }
            return render(request, template, context)

@login_required
def edit_manufacturer(request, pk):
    """ 
    Edit a manufacturer in the store
    """
    query = None
    sort = None
    direction = None
    
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(
                request, "You didn't enter any search criteria!")
            return redirect(reverse('checkout'))

        queries = Q(
            name__icontains=query) | Q(description__icontains=query)
        product = Product.objects.all()
        products = product.filter(queries)

        current_sorting = f'{sort}_{direction}'
                
        context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting,
        }
        return render(
            request, 'products/products.html', context)
    else:
        if not request.user.is_superuser:
            messages.error(request, 'Only staff have access to this feature.')
            return redirect(reverse('home'))

        manufacturer = get_object_or_404(Manufacturer, pk=pk)  

        if request.method == 'POST':
            form = ManufacturerForm(request.POST,instance=manufacturer)
            if form.is_valid():
                form.save()
                messages.success(request, f'You have succesfully updated manufacturer {manufacturer.name}')
                template_name = 'storeowners/manufacturer_and_category_list.html'
                manufacturers = Manufacturer.objects.all()
                categories = Category.objects.all()
                context = {
                    'manufacturers': manufacturers,
                    'categories': categories,
                    'stop_toast_cart': True,
                }
                return render(request, template_name, context)
            else:
                messages.error(request, f'Failed to update manufacturer. Please check your data is valid')
        else:    
            form = ManufacturerForm(instance=manufacturer)
            messages.info(request, f'You are currently editing {manufacturer.name}')

        template = 'storeowners/edit_manufacturer.html'
        context = {
            'form': form,
            'manufacturer': manufacturer,
            'stop_toast_cart': True,
        }
        return render(request, template, context)


class DeleteManufacturer(TemplateView):
    """
    Delete a manufacturer from the store
    """    
    def get(self, request, pk):
        query = None
        sort = None
        direction = None
        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('checkout'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            product = Product.objects.all()
            products = product.filter(queries)

            current_sorting = f'{sort}_{direction}'
                    
            context = {
            'products': products,
            'search_term': query,
            'current_sorting': current_sorting,
            }
            return render(
                request, 'products/products.html', context)
        else:
            manufacturer = get_object_or_404(Manufacturer, pk=pk)
            if request.user.is_superuser:        
                template_name = 'storeowners/delete_manufacturer.html'
                messages.info(request, f'You are currently deleting {manufacturer.name}')
                context = {
                    'manufacturer': manufacturer,
                    'stop_toast_cart': True,
                    }
                return render(request, template_name, context)
            else:
                messages.error(request, 'Only staff have access to this feature.') 
                return redirect(reverse('stock_management'))

    def post(self, request, pk): 
        if request.user.is_superuser:        
            manufacturer = get_object_or_404(Manufacturer, pk=pk)
            manufacturer.delete()
            messages.success(request, 'You have successfully deleted your manufacturer.')        
            template_name = 'storeowners/manufacturer_and_category_list.html'
            manufacturers = Manufacturer.objects.all()
            categories = Category.objects.all()
            context = {
                'manufacturers': manufacturers,
                'categories': categories,
                'stop_toast_cart': True,
            }
            return render(request, template_name, context)
        else:
            messages.error(request, 'Only staff have access to this feature.') 
            return redirect(reverse('stock_management'))
        

@login_required
def add_category(request):
    """ 
    Add a category to the store
    """
    query = None
    sort = None
    direction = None
    
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(
                request, "You didn't enter any search criteria!")
            return redirect(reverse('checkout'))

        queries = Q(
            name__icontains=query) | Q(description__icontains=query)
        product = Product.objects.all()
        products = product.filter(queries)

        current_sorting = f'{sort}_{direction}'
                
        context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting,
        }
        return render(
            request, 'products/products.html', context)
    else:
        if not request.user.is_superuser:
            messages.error(request, 'Only staff have access to this feature.')
            return redirect(reverse('stock_management'))

        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your category has been succesfully added.')
                template_name = 'storeowners/manufacturer_and_category_list.html'
                manufacturers = Manufacturer.objects.all()
                categories = Category.objects.all()
                context = {
                    'manufacturers': manufacturers,
                    'categories': categories,
                    'stop_toast_cart': True,
                }
                return render(request, template_name, context)
                    
            else:
                messages.error(request, 'Failed to add category. Please check your form details.')
        else:
            form = ManufacturerForm()
            template = 'storeowners/add_category.html'
            context = {
                'form': form,
                'stop_toast_cart': True,
            }
            return render(request, template, context)

@login_required
def edit_category(request, pk):
    """ 
    Edit a category in the store
    """
    query = None
    sort = None
    direction = None
    
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(
                request, "You didn't enter any search criteria!")
            return redirect(reverse('checkout'))

        queries = Q(
            name__icontains=query) | Q(description__icontains=query)
        product = Product.objects.all()
        products = product.filter(queries)

        current_sorting = f'{sort}_{direction}'
                
        context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting,
        }
        return render(
            request, 'products/products.html', context)
    else:
        if not request.user.is_superuser:
            messages.error(request, 'Only staff have access to this feature.')
            return redirect(reverse('stock_management'))

        category = get_object_or_404(Category, pk=pk)  

        if request.method == 'POST':
            form = CategoryForm(request.POST, instance=category)
            if form.is_valid():
                form.save()
                messages.success(request, f'You have succesfully updated category {category.name}')
                template_name = 'storeowners/manufacturer_and_category_list.html'
                manufacturers = Manufacturer.objects.all()
                categories = Category.objects.all()
                context = {
                    'manufacturers': manufacturers,
                    'categories': categories,
                    'stop_toast_cart': True,
                }
                return render(request, template_name, context)
            else:
                messages.error(request, f'Failed to update category. Please check your data is valid')
        else:    
            form = CategoryForm(instance=category)
            messages.info(request, f'You are currently editing {category.name}')

            template_name = 'storeowners/edit_category.html'
            context = {
                'form': form,
                'category': category,
                'stop_toast_cart': True,
            }
            return render(request, template_name , context)


class DeleteCategory(TemplateView):
    """
    Class based view to Delete a category from the store, 
    used to render confirmation page prior to deleting
    """    
    def get(self, request, pk):
        query = None
        sort = None
        direction = None
        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('checkout'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            product = Product.objects.all()
            products = product.filter(queries)

            current_sorting = f'{sort}_{direction}'
                    
            context = {
            'products': products,
            'search_term': query,
            'current_sorting': current_sorting,
            }
            return render(
                request, 'products/products.html', context)
        else:

            category = get_object_or_404(Category, pk=pk)

            if request.user.is_superuser:        
                template_name = 'storeowners/delete_category.html'
                messages.info(request, f'You are currently deleting {category.name}')
                context = {
                    'category': category,
                    'stop_toast_cart': True,
                    }
                return render(request, template_name, context)
            else:
                messages.error(request, 'Only staff have access to this feature.') 
                return redirect(reverse('stock_management'))

    def post(self, request, pk): 
        if request.user.is_superuser:        
            category = get_object_or_404(Category, pk=pk)
            category.delete()
            messages.success(request, 'You have successfully deleted your category.')        
            template_name = 'storeowners/manufacturer_and_category_list.html'
            manufacturers = Manufacturer.objects.all()
            categories = Category.objects.all()
            context = {
                'manufacturers': manufacturers,
                'categories': categories,
                'stop_toast_cart': True,
            }
            return render(request, template_name, context)
        else:
            messages.error(request, 'Only staff have access to this feature.') 
            return redirect(reverse('stock_management'))
        
  



