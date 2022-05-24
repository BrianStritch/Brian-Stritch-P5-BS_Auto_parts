from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,        
        'stripe_public_key': 'pk_test_51L2kJDFe61CNoFimnkCIY2EHIthg1GzRGHUpIXHcjcQWlNrEZ0b09VeF0n9D8rkZhih6YTfbAtT6reUOZSJ3GLtL00iIgRfHze',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
