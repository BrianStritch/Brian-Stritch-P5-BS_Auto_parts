from .models import ForumCategory, ForumPost, ForumPostComment, ForumTopics
from forum.forms import ForumCategoryForm, ForumPostCommentForm, ForumTopicsForm, CreateForumPostForm
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from products.models import Product, Category, Manufacturer


def forum(request):
    products = Product.objects.all()
    makes = Manufacturer.objects.all().order_by('name')
    template_name = 'forum/forum.html'
    form = CreateForumPostForm
    forum_categories = ForumCategory.objects.all()
    topics = ForumTopics.objects.all()

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
            'form':form,
            'products': products,
            'makes':makes,
            'search_term': query,
            'current_categories': categories,
            'current_sorting': current_sorting,
        }
        return render(request, 'products/products.html', context)

    else:
        
        categories = ForumCategory.objects.all()
        topics = ForumTopics.objects.all()
        forum_post = ForumPost.objects.all()

        context = {
            'form':form,
            'categories': forum_categories,
            'topics': topics,
            'post': forum_post,
        }
    return render(request, template_name, context)


def Topic_detail(request, slug):
    """ 
    A view to show individual product details
    """
    topics = get_object_or_404(ForumTopics, slug=slug)
    
    liked = False
    try:
      
      queryset = ForumPost.objects.filter(status=1)  
      review = get_object_or_404(queryset, product=product_id )
      comments = review.product_review_comments.filter(approved=True).order_by('created_on') 
      liked = False
      if review.likes.filter(id=request.user.id).exists():
          liked = True
      query = comments.filter(name=request.user)
      commented = False
      if query:
        commented = True
      try:
        favourites = get_object_or_404(Favourites, products=products)
        
      except:
        favourites = False
        

      context = {
      'product': products,
      "comments": comments,
      'review': review,
      "commented": commented,
      "liked": liked,
      'favourites': favourites,
      }
    except:
      try:
        favourites = get_object_or_404(Favourites, products=products)
        
      except:
        favourites = False

      context = {
        'product': products,
        'favourites': favourites,
      }
    return render(request, 'products/product_detail.html', context)
