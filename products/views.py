""" products views.py """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.db.models import Q
from django.views.generic import TemplateView
from .models import Product, Category, Manufacturer
from .forms import ProductForm
from productreviews.models import ProductReview
from favourites.models import Favourites


def all_products(request):
    """
    A view to show all products,
    including sorting and search queries
    """
    products = Product.objects.all()
    makes = Manufacturer.objects.all().order_by('name')
    query = None
    categories = None
    sort = None
    direction = None
    sale = None
    category = 1
    q = 1

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            if categories.count() <= 1:
                category = request.GET['category']
            else:
                category = 1

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

        if 'make' in request.GET:
            query = request.GET['make']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('products'))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = makes.filter(queries)

        if 'sale' in request.GET:
            sale = request.GET['sale']
        if not sale:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('products'))

        products = Product.objects.all().filter(on_sale=True)

    favourites = Favourites.objects.all()
    current_sorting = f'{sort}_{direction}'

    context = {
        'notfav': False,
        'products': products,
        'makes': makes,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'favourites': favourites,
        'category': category,
    }
    return render(request, 'products/products.html', context)


class Product_detail(TemplateView):
    template_name = 'products/product_detail.html'

    def get(self, request, product_id):
        """
        A view to show individual product details
        """
        template_name = 'products/product_detail.html'
        query = None
        sort = None
        direction = None

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('checkout'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            product = Product.objects.all()
            products = product.filter(queries)

            current_sorting = f'{sort}_{direction}'

            context = {
                'products': products,
                'search_term': query,
                'current_sorting': current_sorting,
            }
            return render(request, 'products/products.html', context)
        else:
            product = get_object_or_404(Product, pk=product_id)
            reviews = ProductReview.objects.filter(
                product=product).order_by('-created_on')
            liked = False
            try:
                favourites = get_object_or_404(Favourites, products=products)

            except:
                favourites = False

            context = {
                'reviews': reviews,
                'product': product,
                "liked": liked,
                'favourites': favourites,
            }
            template_name = 'products/product_detail.html'
            return render(request, template_name, context)


@login_required
def add_product(request):
    """
    Add a product to the store
    """
    query = None
    sort = None
    direction = None

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('checkout'))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        product = Product.objects.all()
        products = product.filter(queries)

        current_sorting = f'{sort}_{direction}'

        context = {
            'products': products,
            'search_term': query,
            'current_sorting': current_sorting,
        }
        return render(request, 'products/products.html', context)
    else:
        if not request.user.is_superuser:
            messages.error(request, 'Only staff have access to this feature.')
            return redirect(reverse('home'))

        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save()
                messages.success(request,
                                 'Your product has been succesfully added.')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(
                    request,
                    'Failed to add product. Please check your form details.')
        else:
            form = ProductForm()
            template = 'products/add_product.html'
            context = {
                'form': form,
                'stop_toast_cart': True,
            }
            return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store
    """
    query = None
    sort = None
    direction = None

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('checkout'))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        product = Product.objects.all()
        products = product.filter(queries)

        current_sorting = f'{sort}_{direction}'

        context = {
            'products': products,
            'search_term': query,
            'current_sorting': current_sorting,
        }
        return render(request, 'products/products.html', context)
    else:
        if not request.user.is_superuser:
            messages.error(request, 'Only staff have access to this feature.')
            return redirect(reverse('home'))

        product = get_object_or_404(Product, pk=product_id)

        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    f'You have succesfully updated product {product.name}')

                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(
                    request,
                    'Failed to update product. Please check your data is valid'
                )
        else:
            form = ProductForm(instance=product)
            messages.info(request, f'You are currently editing {product.name}')
            template = 'products/edit_product.html'
            context = {
                'form': form,
                'product': product,
                'stop_toast_cart': True,
            }
            return render(request, template, context)


class DeleteProduct(TemplateView):
    """
    Delete a product from the store
    """

    def get(self, request, product_id):
        query = None
        sort = None
        direction = None

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('checkout'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            product = Product.objects.all()
            products = product.filter(queries)

            current_sorting = f'{sort}_{direction}'

            context = {
                'products': products,
                'search_term': query,
                'current_sorting': current_sorting,
            }
            return render(request, 'products/products.html', context)
        else:
            product = get_object_or_404(Product, pk=product_id)
            if request.user.is_superuser:
                template_name = 'products/delete_product.html'
                messages.info(request,
                              f'You are currently deleting {product.name}')
                context = {
                    'product': product,
                    'stop_toast_cart': True,
                }
                return render(request, template_name, context)
            else:
                messages.error(request,
                               'Only staff have access to this feature.')
                return redirect(reverse('home'))

    def post(self, request, product_id):
        if request.user.is_superuser:
            product = get_object_or_404(Product, pk=product_id)
            product.delete()
            messages.success(request,
                             'You have successfully deleted your product.')
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Only staff have access to this feature.')
            return redirect(reverse('home'))
