# imports
# 3rd party imports from django
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import generic, View
from django.db.models import Q

# internal imports from BS_Auto_parts
from products.models import Product
from .models import Favourites
from .forms import Favouriteform



@login_required
def view_favourites(request):
    """
    A view that displays users favourites
    
    """
    template_name = 'favourites/favourites.html'
    favourites = Favourites.objects.filter(username=request.user)
    context = {
        'favourites': favourites,
    }
    return render(request, template_name, context)


class ToggleFavourite(View):
    """
        Class based view to toggle the favourite status for
        the selected product and user and saving to the database.
    """
    
    def post(self, request, pk):
        
        """
        POST request for processing the favourite status
        data passed from the reviews details page and if
        form is valid updates and saves status to database.
        """
        product = get_object_or_404(Product, id=pk)
        
        try:
            favourite = get_object_or_404(Favourites, products=pk)
            print('found favourite', favourite)
            favourite.delete()
            messages.success(request, '\
                You have succesfully removed this product from your favourites.')
            return HttpResponseRedirect(reverse('product_detail', args=[pk]))
        except:            
            Favourites.objects.create(
                username = request.user,
                products = product
            )
            messages.success(request, '\
                You have succesfully added this product to your favourites.')
            return HttpResponseRedirect(reverse('product_detail', args=[pk]))

        return HttpResponseRedirect(reverse('product_detail', args=[pk]))
    



