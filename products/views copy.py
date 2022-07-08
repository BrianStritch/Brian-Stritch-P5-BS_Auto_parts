from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.db.models import Q
from django.views.generic import TemplateView, UpdateView, DeleteView
from .models import Product, Category, Manufacturer
from .forms import ProductForm
from productreviews.models import ProductReview, ProductReviewComment
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
    q=1
    # current_sorting = None,None

    if request.GET:
      

      if 'sort' in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey
        if sortkey == 'name':
          sortkey = 'lower_name'
          products = products.annotate(lower_name = Lower('name'))
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
      'makes':makes,
      'search_term': query,
      'current_categories': categories,
      'current_sorting': current_sorting,
      'favourites': favourites,
      'category':category,
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
        products = get_object_or_404(Product, pk=product_id)    # gets the product  
        liked = False
        count = ProductReview.objects.filter(product=product_id, status=1).count() #counts published reviews
        print('count start', count)
        if count == 1 : # if published reviews == 1
          review_length = True # sets bool for template to display singular occurrance
          product = get_object_or_404(Product, pk=product_id)
          review = get_object_or_404(ProductReview, product=product)
          print('review =', review)
          
          nancount = ProductReviewComment.objects.filter(product_review=review).count()
          print('nancount =', nancount)
          # comments = None
          if nancount <= 1:
            print('nancount == 1')
            queryset = ProductReview.objects.filter(status=1)
            print('1', queryset) 
            reviews = get_object_or_404(queryset, product=product_id)
            print('review = ', reviews)
            comments = reviews.product_review_comments.filter(approved=True).order_by('-created_on')
            print('comments', comments)
            liked = False
          
            if review.likes.filter(id=request.user.id).exists():
                liked = True
            # try:
            #     comments = review.comments.filter(approved=True).order_by('created_on')
            # except:
            #     comments = None
            liked = False
            if review.likes.filter(id=self.request.user.id).exists():
                liked = True
            
            if query:
              commented = True
            try:
                favourites = get_object_or_404(Favourites, products=products)
                
            except:
              favourites = False
          
            print('product = ',product)
            print('review = ',review)
            print('end comments = ', comments)
            context = {
                'review_length':review_length,
                'review':review,
                'product': product,
                "comments": comments,
                "commented": False,
                "liked": liked,
                'favourites': favourites,         
              }
            template_name = 'products/product_detail.html'
            return render(request, template_name, context)
          else:
            print('nancount lge')
            queryset = ProductReview.objects.filter(status=1)
            print('1', queryset) 
            reviews = get_object_or_404(queryset, product=product_id)
            print('review = ', reviews)
            comments = reviews.product_review_comments.filter(approved=True).order_by('-created_on')
            print('comments', comments)
            liked = False
          
            if review.likes.filter(id=request.user.id).exists():
                liked = True
            # try:
            #     comments = review.comments.filter(approved=True).order_by('created_on')
            # except:
            #     comments = None
            liked = False
            if review.likes.filter(id=self.request.user.id).exists():
                liked = True
            
            if query:
              commented = True
            try:
                favourites = get_object_or_404(Favourites, products=products)
                
            except:
              favourites = False
          
            print('product = ',product)
            print('review = ',review)
            print('end comments = ', comments)
            context = {
                'review_length':review_length,
                'review':review,
                'product': product,
                "comments": comments,
                "commented": False,
                "liked": liked,
                'favourites': favourites,         
              }
            template_name = 'products/product_detail.html'
            return render(request, template_name, context)


          # review_count = 

          # except:
          #   try:
          #     favourites = get_object_or_404(Favourites, products=products)
              
          #   except:
          #     favourites = False

          #   review_length = False
          #   print('before end 1')
          #   # review = ProductReview.objects.get(product=product_id)
          #   # print('review.title, body', review.product_id, review.content)

          #   context = {          
          #     'reviews_length':review_length,
          #     'review':review,
          #     'product': products,
          #     'favourites': favourites,
          #     'review': review,
          #   }
          # return render(request, 'products/product_detail.html', context)
        
        elif count > 1:
          print('count is 2')
          review_length = False
          product = get_object_or_404(Product, pk=product_id)
          reviews = ProductReview.objects.all()
          new_count = ProductReview.objects.filter(product=product_id).count()
          try:
              favourites = get_object_or_404(Favourites, products=products)
              
          except:
            favourites = False

          # query = comments.filter(name=request.user)
          commented = False
          if query:
            commented = True 

          print('new_count = ',new_count)
          print('product = ',product)
          print('reviews = ',reviews)
          context = {
              'reviews_length':review_length,
              'reviews':reviews,
              'product': product,
              "commented": False,
              "liked": False,
              'favourites': favourites,         
            }
          template_name = 'products/product_detail.html'
          return render(request, template_name, context)
        
        else:
          print('count is 0')
          review_length = False
          product = get_object_or_404(Product, pk=product_id)
          try:
              favourites = get_object_or_404(Favourites, products=products)
              
          except:
            favourites = False

          print('product 3= ',product)
          context = {
              'reviews_length':review_length,
              'product': product,
              "commented": False,
              "liked": False,
              'favourites': favourites,         
            }
          template_name = 'products/product_detail.html'
          return render(request, template_name, context)
            
            
            

          


  # def product_detail(request, product_id):
  #     """ 
  #     A view to show individual product details
  #     """
  #     query = None
  #     sort = None
  #     direction = None

  #     if 'q' in request.GET:
  #       query = request.GET['q']
  #       if not query:
  #         messages.error(
  #         request, "You didn't enter any search criteria!")
  #         return redirect(reverse('checkout'))

  #       queries = Q(
  #       name__icontains=query) | Q(description__icontains=query)
  #       product = Product.objects.all()
  #       products = product.filter(queries)

  #       current_sorting = f'{sort}_{direction}'

  #       context = {
  #       'products': products,
  #       'search_term': query,
  #       'current_sorting': current_sorting,
  #       }
  #       return render(
  #       request, 'products/products.html', context)
  #     else:
  #       products = get_object_or_404(Product, pk=product_id)      
  #       liked = False
  #       count = ProductReview.objects.filter(product=product_id).count()
  #       print('count start', count)
  #       if count <=1 :
  #         try:
  #           review_length = True
  #           review = ProductReview.objects.all().filter(product=product_id)
  #           # review = ProductReview.objects.filter(product=product_id)
  #           print('review =', review)
  #           reviews = ProductReview.objects.get(product=product_id)
  #           print('reviews =', reviews)
  #           comments = reviews.product_review_comments.all().order_by('created_on')          
            
            

  #           print('past comments') 
            
  #           liked = False
            
  #           if review.likes.filter(id=request.user.id).exists():
  #               liked = True
            
  #           query = comments.filter(name=request.user)
  #           commented = False
  #           if query:
  #             commented = True 
  #           try:
  #             favourites = get_object_or_404(Favourites, products=products)
              
  #           except:
  #             favourites = False
            
  #           print('review length 2= ', review_length)  
  #           print('review 2 = ', review)  


  #           context = {
  #             'reviews_length':review_length,
  #             'review':review,
  #             'product': products,
  #             "comments": comments,
  #             'reviews': reviews,
  #             "commented": commented,
  #             "liked": liked,
  #             'favourites': favourites,         
  #           }
  #           print('************************************************')
  #           print('reviews_length', review_length,)
  #           print('review', review)
  #           print( 'product', products)
  #           print("comments", comments)
  #           print( 'reviews', reviews)
  #           print( "commented", commented)
  #           print("liked", liked)
  #           print('favourites', favourites)
  #           print('before return')
  #           return render(request, 'products/product_detail.html', context)
  #         except:
  #           try:
  #             favourites = get_object_or_404(Favourites, products=products)
              
  #           except:
  #             favourites = False

  #           review_length = False
  #           print('before end 1')
  #           # review = ProductReview.objects.get(product=product_id)
  #           # print('review.title, body', review.product_id, review.content)

  #           context = {          
  #             'reviews_length':review_length,
  #             'review':review,
  #             'product': products,
  #             'favourites': favourites,
  #             'review': review,
  #           }
  #         return render(request, 'products/product_detail.html', context)
        
  #       else:
  #         try:
            
  #           review_length = False
  #           queryset = ProductReview.objects.all().filter(pk=product_id)  
  #           print('queryset2 = ', queryset) 
  #           reviews = get_object_or_404(queryset, product=product_id )       
  #           comments = reviews.product_review_comments.all().order_by('created_on')
            

  #           print('past comments') 
            
  #           liked = False
            
  #           if reviews.likes.filter(id=request.user.id).exists():
  #               liked = True
            
  #           query = comments.filter(name=request.user)
  #           commented = False
  #           if query:
  #             commented = True 
  #           try:
  #             favourites = get_object_or_404(Favourites, products=products)
              
  #           except:
  #             favourites = False
            
  #           print('review length 2= ', review_length)  
  #           print('review 2 = ', review)  


  #           context = {
  #             'reviews_length':review_length,
  #             'review':review,
  #             'product': products,
  #             "comments": comments,
  #             'reviews': reviews,
  #             "commented": commented,
  #             "liked": liked,
  #             'favourites': favourites,         
  #           }
  #         except:
  #           try:
  #             favourites = get_object_or_404(Favourites, products=products)
              
  #           except:
  #             favourites = False

  #           review_length = True
  #           print('before end')
  #           review = ProductReview.objects.all().filter(product=product_id)
  #           print('review.title, body', review.product_id, review.content)

  #           context = {          
  #             'reviews_length':review_length,
  #             'review':review,
  #             'product': products,
  #             'favourites': favourites,
  #             'review': review,
  #           }
  #         return render(request, 'products/product_detail.html', context)


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

    if request.method == 'POST':
      form = ProductForm(request.POST, request.FILES)
      if form.is_valid():
        product = form.save()
        messages.success(request, 'Your product has been succesfully added.')
        return redirect(reverse('product_detail', args=[product.id ]))      
      else:
        messages.error(request, 'Failed to add product. Please check your form details.')
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

    product = get_object_or_404(Product, pk=product_id)  

    if request.method == 'POST':
      form = ProductForm(request.POST, request.FILES, instance=product)
      if form.is_valid():
        form.save()
        messages.success(request, f'You have succesfully updated product {product.name}')
        
        return redirect(reverse('product_detail', args=[product.id ]))
      else:
        messages.error(request, f'Failed to update product. Please check your data is valid')
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
          product = get_object_or_404(Product, pk=product_id)
          if request.user.is_superuser:        
            template_name = 'products/delete_product.html'
            messages.info(request, f'You are currently deleting {product.name}')
            context = {
                'product': product,
                'stop_toast_cart': True,
                }
            return render(request, template_name, context)
          else:
              messages.error(request, 'Only staff have access to this feature.') 
              return redirect(reverse('home'))

    def post(self, request, product_id): 
        if request.user.is_superuser:        
          product = get_object_or_404(Product, pk=product_id)
          product.delete()
          messages.success(request, 'You have successfully deleted your product.')        
          return redirect(reverse('products'))
        else:
            messages.error(request, 'Only staff have access to this feature.') 
            return redirect(reverse('home'))
        
    