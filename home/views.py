# imports
# 3rd party imports from django
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

# internal imports from BS_Auto_parts
from products.models import Product, Category, Manufacturer
from newsletter.forms import NewsletterSignupForm

def home(request):
    """
    A view to return the home page
    """
    newsletter_form = NewsletterSignupForm()
    template = 'home/index.html'
    home = True
    context = {
        'form':newsletter_form,
        'home': home,
        'bttoff':True
    }
    return render(request, template, context)

def shop(request):
    """
    A view to return the home page
    """
    makes = Manufacturer.objects.all().order_by('name')   

    context = {
        'makes': makes,
        'bttoff':True,
        
    }
    return render(request,'home/shop.html', context)    
