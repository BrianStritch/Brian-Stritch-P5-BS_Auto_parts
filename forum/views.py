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


def Topic_list(request, slug, *args , **kwargs ):
    """ 
    A view to show individual product details
    """
    # topic = get_object_or_404(ForumTopics, slug=slug)
    # forum_post = get_object_or_404(ForumPost, topic=topic )
    # post = ForumPost.objects.filter(status=1)  
    topic = get_object_or_404(ForumTopics, slug=slug)
    # topic = ForumTopics.objects.filter()  
    #  queryset= get_object_or_404(queryset, )
    
    posts = ForumPost.objects.all()

    
    
    template_name = 'forum/topic_details.html'
    context = {
    # "comments": comments,
    'posts': posts,
    # "commented": commented,
    # "liked": liked,
    'topic': topic,
    }
          
    return render(request, template_name, context)

def PostDetail(request, slug, *args , **kwargs):
    post = get_object_or_404(ForumPost, slug=slug)
    #   topic = get_object_or_404(ForumTopics, topic=request.topic)
    template_name = 'forum/post_detail.html'    
        
    comments = post.forum_post_comments.filter(approved=True).order_by('created_on') 
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True
    query = comments.filter(name=request.user)
    commented = False
    if query:
        commented = True
    context = {
        
        'post': post,
        "commented": commented,
        "liked": liked,
        'comments': comments,
        }
    return render(request, template_name, context)
