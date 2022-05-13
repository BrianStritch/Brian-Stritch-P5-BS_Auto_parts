from django.shortcuts import render
from products.models import Manufacturer

def index(request):
    """
    A view to return the home page
    """
    makes = Manufacturer.objects.all().order_by('name')    

    context = {
        'makes': makes,
    }
    return render(request,'home/index.html', context)

