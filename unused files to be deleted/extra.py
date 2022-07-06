
from django.db.models import Q


query = None
sort = None
direction = None
 
if 'q' in request.GET:
query = request.GET['q']
if not query:
    messages.error(
        request, "You didn't enter any search criteria!")
    return redirect(reverse('products'))

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


from django.db.models import Q

    else:

        
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