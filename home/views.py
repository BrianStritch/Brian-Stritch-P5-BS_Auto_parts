from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from products.models import Product, Category, Manufacturer
from newsletter.forms import NewsletterSignupForm

def home(request):
    products = Product.objects.all()
    makes = Manufacturer.objects.all().order_by('name')
    newsletter_form = NewsletterSignupForm()

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
        
        if 'make' in request.GET:
            query = request.GET['make']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
        
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        current_sorting = f'{sort}_{direction}'

        context = {
        'newsletter_form':newsletter_form,
        'products': products,
        'makes':makes,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        }
        return render(request, 'products/products.html', context)

    else:
        """
        A view to return the home page
        """
        
        template = 'home/home.html'
        home = True
        context = {
            'form':newsletter_form,
            'home': home,
            'bttoff':True
        }
        return render(request, template, context)

def index(request):
    products = Product.objects.all()
    makes = Manufacturer.objects.all().order_by('name')

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
        
        if 'make' in request.GET:
            query = request.GET['make']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
        
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        current_sorting = f'{sort}_{direction}'

        context = {
        'products': products,
        'makes':makes,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        }
        return render(request, 'products/products.html', context)

    else:
        """
        A view to return the home page
        """
        makes = Manufacturer.objects.all().order_by('name')    

        context = {
            'makes': makes,
            'bttoff':True,
            
        }
        return render(request,'home/index.html', context)    
    