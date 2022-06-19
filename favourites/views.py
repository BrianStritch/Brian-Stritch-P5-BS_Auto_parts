from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from products.models import Product
# from util.util import setup_pagination
from .models import Favourites



@login_required
def view_favourites(request):
    """
    A view that displays users favourites
    
    """
    template_name = 'favourites/favourites.html'
    products = Product.objects.all()
    context = {
        'favourites': products,
    }
    return render(request, template_name, context)
    

    



