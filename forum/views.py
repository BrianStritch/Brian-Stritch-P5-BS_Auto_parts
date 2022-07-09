# imports
# 3rd party imports from django
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import TemplateView, UpdateView, DeleteView
from django.contrib import messages
from django.db.models import Q
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# internal imports from BS_Auto_parts
from products.models import Product, Category, Manufacturer
from .models import ForumCategory, ForumPost, ForumPostComment, ForumTopics
from forum.forms import ForumCategoryForm, ForumPostCommentForm
from forum.forms import ForumTopicsForm, CreateForumPostForm

@login_required
def forum(request):
    """
    Renders a view displaying all forum categories with main
    topic headings
    # """
    # products = Product.objects.all()
    # makes = Manufacturer.objects.all().order_by('name')
    template_name = 'forum/forum.html'
    form = CreateForumPostForm
    forum_categories = ForumCategory.objects.all()
    topics = ForumTopics.objects.all()

    # query = None
    # categories = None
    # sort = None
    # direction = None

    # if request.GET:

    #     if 'q' in request.GET:
    #         query = request.GET['q']
    #         if not query:
    #             messages.error(request, "\
    #                 You didn't enter any search criteria!")
    #             return redirect(reverse('products'))
            
    #         queries = Q(name__icontains=query) | Q(description__icontains=query)
    #         products = products.filter(queries)
        
    #     if 'make' in request.GET:
    #         query = request.GET['make']
    #         if not query:
    #             messages.error(request, "\
    #                 You didn't enter any search criteria!")
    #             return redirect(reverse('products'))
        
    #         queries = Q(name__icontains=query) | Q(description__icontains=query)
    #         products = products.filter(queries)

    #     current_sorting = f'{sort}_{direction}'

    #     context = {
    #         'form':form,
    #         'products': products,
    #         'makes':makes,
    #         'search_term': query,
    #         'current_categories': categories,
    #         'current_sorting': current_sorting,
    #     }
    #     return render(request, 'products/products.html', context)

    # else:
        
    categories = ForumCategory.objects.all()
    topics = ForumTopics.objects.all()
    forum_post = ForumPost.objects.all()

    context = {
        'form':form,
        'categories': forum_categories,
        'topics': topics,
        'post': forum_post,            
        'stop_toast_cart': True,
        'forum':True,
    }
    return render(request, template_name, context)

def Topic_list(request, slug, *args , **kwargs ):
    """ 
    A view to list all posts relating to the selected
    topic
    """ 
    # query = None
    # sort = None
    # direction = None
    
    # if 'q' in request.GET:
    #     query = request.GET['q']
    #     if not query:
    #         messages.error(
    #             request, "You didn't enter any search criteria!")
    #         return redirect(reverse('checkout'))

    #     queries = Q(
    #         name__icontains=query) | Q(description__icontains=query)
    #     product = Product.objects.all()
    #     products = product.filter(queries)

    #     current_sorting = f'{sort}_{direction}'
                
    #     context = {
    #     'products': products,
    #     'search_term': query,
    #     'current_sorting': current_sorting,
    #     }
    #     return render(
    #         request, 'products/products.html', context)
    # else:
    topic = get_object_or_404(ForumTopics, slug=slug)    
    posts = ForumPost.objects.all()    
    
    template_name = 'forum/topic_details.html'
    context = {
    'posts': posts,
    'topic': topic,
    'stop_toast_cart': True,
    'forum':True,
    }
          
    return render(request, template_name, context)

def PostDetail(request, pk, *args , **kwargs):
    '''
    renders a view to display forum post detail relating
    to the specific post selected
    '''
    

    post = get_object_or_404(ForumPost, pk= pk)
    template_name = 'forum/post_detail.html'
        
    
    post_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post_liked = True
        
    comments = post.forum_post_comments.filter(
        approved=True
        ).order_by('created_on')
    comments_liked = comments.filter(likes=True)

    query = comments.filter(name=request.user)
    commented = False
    if query:
        commented = True
    context = {
        'comments_liked':comments_liked,
        'post': post,
        "commented": commented,
        "post_liked": post_liked,
        'comments': comments,
        'stop_toast_cart': True,
        'forum':True,
        }
    return render(request, template_name, context)

###############################  Forum Categories  #######################
class CreateCategory(TemplateView):

    def get(self, request):
        """ 
        Add a Category to the Forum
        # """
        
        if not request.user.is_superuser:
            messages.error(request, '\
                Only staff have access to this feature.')
            forum_categories = ForumCategory.objects.all()
            topics = ForumTopics.objects.all() 
            template_name = 'forum/forum.html'
            context = {                
                'categories': forum_categories,
                'topics': topics,
                'forum': True,
                'stop_toast_cart': True,
                }
            return render(request, template_name, context)

        form = ForumCategoryForm
        template_name = 'forum/create_forum_category.html'

        context = {
            'form': form,
            'stop_toast_cart': True,
            'forum':True,
        }
        return render(request, template_name, context)

    def post(self, request):        
        form = ForumCategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, '\
                Your category has been succesfully added.')            
            forum_categories = ForumCategory.objects.all()
            topics = ForumTopics.objects.all()
            template_name = 'forum/forum.html'
            context = {
                'categories': forum_categories,
                'topics': topics,
                'forum': True,
                'stop_toast_cart': True,
                }
            return render(request, template_name, context)
       
        else:
            messages.error(request, '\
                Failed to add Category. Please check your form details.')
            form = ForumCategoryForm()
            template = 'forum/create_forum_category.html'
            context = {
                'form': form,
                'stop_toast_cart': True,
                'forum':True,
            }
            return render(request, template, context)


class EditCategory(TemplateView):
    """ 
    Edit a category in the forum
    """
    def get(self, request, pk): 
        
        category = get_object_or_404(ForumCategory, pk=pk) 
        form = ForumCategoryForm(instance=category)
        if not request.user.is_superuser:
            messages.error(request, '\
                Only staff have access to this feature.')
            forum_categories = ForumCategory.objects.all()
            topics = ForumTopics.objects.all()  
            template_name = 'forum/forum.html'
            context = {                               
                'categories': forum_categories,
                'topics': topics,
                'forum': True,
                'stop_toast_cart': True,
                }
            return render(request, template_name, context)
        template_name = 'forum/edit_forum_category.html'
        messages.info(request, f'\
            You are currently editing {category.name}')
        context = {
            'form':form,
            'forum': True,
            'stop_toast_cart': True,
            }
        return render(request, template_name, context)

    def post(self, request, pk):
        category = get_object_or_404(ForumCategory, pk=pk)
        form = ForumCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, f'\
                You have succesfully updated category {category.name}') 
            forum_categories = ForumCategory.objects.all()
            topics = ForumTopics.objects.all()          
            template = 'forum/forum.html'
            context = {                
                'categories': forum_categories,
                'topics': topics,
                'forum': True,
                'stop_toast_cart': True,
            }
            return render(request, template, context)

        else:
            messages.error(request, f'\
                Failed to update category {category.name}. \
                    Please check your data is valid')        
            form = ForumCategoryForm(instance=category)
            messages.info(request, f'\
                You are currently editing {category.name}')
            template = 'forum/edit_forum_category.html'
            context = {
                'form': form,
                'forum': True,
                'stop_toast_cart': True,
            }
            return render(request, template, context)
  

class DeleteCategory(TemplateView):
    """
    Delete a category in the forum
    """
    def get(self, request, pk):
                
        category = get_object_or_404(ForumCategory, pk=pk)
        if not request.user.is_superuser:
            messages.error(request, '\
                Only staff have access to this feature.')
            forum_categories = ForumCategory.objects.all()
            topics = ForumTopics.objects.all() 
            template_name = 'forum/forum.html'
            context = {                                
                'categories': forum_categories,
                'topics': topics,
                'forum': True,
                'stop_toast_cart': True,
                }
            return render(request, template_name, context)
        template_name = 'forum/delete_forum_category.html'
        messages.info(request, f'\
            You are currently deleting {category.name}')
        context = {
            'forum': True,
            'stop_toast_cart': True,
            }
        return render(request, template_name, context)

    def post(self, request, pk):
        category = get_object_or_404(ForumCategory, pk=pk)
        category.delete()
        messages.success(request, '\
            You have successfully deleted the forum category')
        forum_categories = ForumCategory.objects.all()
        topics = ForumTopics.objects.all() 
        template_name = 'forum/forum.html'
        context = {                                
            'categories': forum_categories,
            'topics': topics,
            'forum': True,
            'stop_toast_cart': True,
            }
        return render(request, template_name, context)
    
###############################  Forum Topics  ###################
class CreateTopic(TemplateView):

    def get(self, request):
        """ 
        Add a Category topic to the Forum
        """
        
        if not request.user.is_superuser:
            messages.error(request, '\
                Only staff have access to this feature.')
            forum_categories = ForumCategory.objects.all()
            topics = ForumTopics.objects.all() 
            template_name = 'forum/forum.html'
            context = {                
                'categories': forum_categories,
                'topics': topics,
                'forum': True,
                'stop_toast_cart': True,
                }
            return render(request, template_name, context)

        form = ForumTopicsForm
        template_name = 'forum/create_forum_topic.html'

        context = {
            'form': form,
            'stop_toast_cart': True,
            'forum':True,
        }
        return render(request, template_name, context)

    def post(self, request):
        
        form = ForumTopicsForm(request.POST)
        if form.is_valid():
            topic = form.save()
            messages.success(request, '\
                Your topic has been succesfully added.')            
            forum_categories = ForumCategory.objects.all()
            topics = ForumTopics.objects.all()
            template_name = 'forum/forum.html'
            context = {
                'categories': forum_categories,
                'topics': topics,
                'forum': True,
                'stop_toast_cart': True,
                }
            return render(request, template_name, context)
       
        else:
            messages.error(request, '\
                Failed to add topic. Please check your form details.')
            form = ForumTopicsForm()
            template = 'forum/create_forum_topic.html'
            context = {
                'form': form,
                'stop_toast_cart': True,
                'forum':True,
            }
            return render(request, template, context)


class EditTopic(TemplateView):
    """ 
    Edit a category topic in the forum
    """
    def get(self, request, pk):
        
        topic = get_object_or_404(ForumTopics, pk=pk) 
        form = ForumTopicsForm(instance=topic)
        if not request.user.is_superuser:
            messages.error(request, 'Only staff have access to this feature.')
            forum_categories = ForumCategory.objects.all()
            topics = ForumTopics.objects.all()  
            template_name = 'forum/forum.html'
            context = {                               
                'categories': forum_categories,
                'topics': topics,
                'forum': True,
                'stop_toast_cart': True,
                }
            return render(request, template_name, context)
        template_name = 'forum/edit_forum_topic.html'
        messages.info(request, f'You are currently editing {topic.name}')
        context = {
            'form':form,
            'forum': True,
            'stop_toast_cart': True,
            }
        return render(request, template_name, context)

    def post(self, request, pk):
        topic = get_object_or_404(ForumTopics, pk=pk)
        form = ForumTopicsForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            messages.success(request, f'\
                You have succesfully updated topic {topic.name}') 
            forum_categories = ForumCategory.objects.all()
            topics = ForumTopics.objects.all()          
            template = 'forum/forum.html'
            context = {                
                'categories': forum_categories,
                'topics': topics,
                'forum': True,
                'stop_toast_cart': True,
            }
            return render(request, template, context)

        else:
            messages.error(request, f'\
                Failed to update topic {topic.name}.\
                     Please check your data is valid')        
            form = ForumCategoryForm(instance=category)
            messages.info(request, f'\
                You are currently editing {topic.name}')
            template = 'forum/edit_forum_topic.html'
            context = {
                'form': form,
                'forum': True,
                'stop_toast_cart': True,
            }
            return render(request, template, context)
  

class DeleteTopic(TemplateView):
    """
    Delete a category in the forum
    """
    def get(self, request, pk): 
              
        topic = get_object_or_404(ForumTopics, pk=pk)
        if not request.user.is_superuser:
            messages.error(request, '\
                Only staff have access to this feature.')
            forum_categories = ForumCategory.objects.all()
            topics = ForumTopics.objects.all() 
            template_name = 'forum/forum.html'
            context = {                                
                'categories': forum_categories,
                'topics': topics,
                'forum': True,
                'stop_toast_cart': True,
                }
            return render(request, template_name, context)
        template_name = 'forum/delete_forum_topic.html'
        messages.info(request, f'\
            You are currently deleting {topic.name}')
        context = {
            'forum': True,
            'stop_toast_cart': True,
            }
        return render(request, template_name, context)

    def post(self, request, pk):
        topic = get_object_or_404(ForumTopics, pk=pk)
        topic.delete()
        messages.success(request, '\
            You have successfully deleted the forum topic')
        forum_categories = ForumCategory.objects.all()
        topics = ForumTopics.objects.all() 
        template_name = 'forum/forum.html'
        context = {                                
            'categories': forum_categories,
            'topics': topics,
            'forum': True,
            'stop_toast_cart': True,
            }
        return render(request, template_name, context)
    

###############################  Forum Posts  ########################## 
class CreatePost(TemplateView):

    def get(self, request, pk):
        """ 
        Add a Post to the Forum topic selected
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
            topic = get_object_or_404(ForumTopics, pk=pk)
            id = topic.id
            form = CreateForumPostForm
            template_name = 'forum/create_forum_post.html'
            
            context = {
                'topic': topic,
                'form': form,
                'stop_toast_cart': True,
                'forum':True,
            }
            return render(request, template_name, context)

    def post(self, request, pk):
        
        form = CreateForumPostForm(request.POST)
        
        if form.is_valid():
            form.instance.author = request.user
            post = form.save()
            slug = post.topic.slug
            messages.success(request, '\
                Your post has been sent to admin for approval and\
                will appear shortly.') 
            return HttpResponseRedirect(reverse('topic_list', args=[slug]))
       
        else:
            messages.error(request, '\
                Failed to add Post. Please check your form details.')
            form = CreateForumPostForm()
            template = 'forum/create_forum_post.html'
            context = {
                'form': form,
                'stop_toast_cart': True,
                'forum':True,
            }
            return render(request, template, context)


class EditPost(TemplateView):
    """ 
    Edit a selected topic post in the forum
    """    
    def get(self, request, pk):
        
        post = get_object_or_404(ForumPost, pk=pk)
        topic = post.topic
        form = CreateForumPostForm(instance=post)        
        template_name = 'forum/edit_forum_post.html'
        messages.info(request, f'\
            You are currently editing {post.title}')
        context = {
            'topic': topic,
            'post': post,
            'form':form,
            'forum': True,
            'stop_toast_cart': True,
            }
        return render(request, template_name, context)

    def post(self, request, pk):
        post = get_object_or_404(ForumPost, pk=pk)
        slug = post.topic.slug
        form = CreateForumPostForm(request.POST, instance=post)
        if form.is_valid():
            form.instance.status = 0           
            form.save()
            messages.success(request, f'\
                You have succesfully updated post {post.title}. \
                Your post has been submitted to admin\
                     for approval and will appear shortly.') 
            return HttpResponseRedirect(reverse('topic_list', args=[slug]))
            

        else:
            messages.error(request, f'\
                Failed to update post {post.title}.\
                     Please check your data is valid') 
            post = get_object_or_404(ForumPost, pk=pk) 
            topic = post.topic      
            form = CreateForumPostForm(instance=post)
            messages.info(request, f'\
                You are currently editing {post.title}')
            template = 'forum/edit_forum_post.html'
            context = {
                'topic': topic,
                'post': post,
                'form': form,
                'forum': True,
                'stop_toast_cart': True,
            }
            return render(request, template, context)
  

class DeletePost(TemplateView):
    """
    Delete a selected topic post in the forum
    """
    def get(self, request, pk):
              
        post = get_object_or_404(ForumPost, pk=pk)
        template_name = 'forum/delete_forum_post.html'
        messages.info(request, f'\
            You are currently deleting {post.title}')
        context = {
            'post': post,
            'forum': True,
            'stop_toast_cart': True,
            }
        return render(request, template_name, context)

    def post(self, request, pk):
        post = get_object_or_404(ForumPost, pk=pk)
        slug = post.title.slug
        post.delete()
        messages.success(request, '\
            You have successfully deleted the forum post')
        return HttpResponseRedirect(reverse('topic_list', args=[slug]))
    

class PostLike(View):
    """
        Class based view to toggle the liked status for
        the selected post and saving to the database.
    """
    def post(self, request, pk):
        """
        POST request for processing the Post liked status
        data passed from the reviews details page and if
        form is valid updates and saves status to database.
        """
        post = get_object_or_404(ForumPost, pk=pk)
        pk = post.pk
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.success(request, '\
                You have succesfully un-liked this post.')
        else:
            post.likes.add(request.user)
            messages.success(request, '\
                You have succesfully liked this post.')

        return HttpResponseRedirect(reverse('post_detail', args=[pk]))

###############################  Forum Post Comments  ###################
class CreateForumComment(TemplateView):

    def get(self, request, pk):
        """ 
        Add a comment to the Forum Post Comment selected
        """
        
        post = get_object_or_404(ForumPost, pk=pk)
        topic = post.topic
        form = ForumPostCommentForm()
        template_name = 'forum/create_forum_comment.html'

        context = {
            'post': post,
            'topic': topic,
            'form': form,
            'stop_toast_cart': True,
            'forum':True,
        }
        return render(request, template_name, context)

    def post(self, request, pk):
        
        form = ForumPostCommentForm(request.POST)
        post = get_object_or_404(ForumPost, pk=pk)        
        pk = post.pk
        if form.is_valid():
            form.instance.post = post
            form.instance.name = request.user.username
            form.instance.email = request.user.email
            post = form.save()
            messages.success(request, '\
                Your comment has been sent to admin for approval and\
                will appear shortly.')            
            return HttpResponseRedirect(reverse('post_detail', args=[pk]))
       
        else:
            messages.error(request, '\
                Failed to add Comment. Please check your form details.')
            form = ForumPostCommentForm()
            post = get_object_or_404(ForumPost, pk=pk)
            topic = post.topic
            template = 'forum/create_forum_comment.html'
            context = {
                'post': post,
                'topic': topic,
                'form': form,
                'stop_toast_cart': True,
                'forum':True,
            }
            return render(request, template, context)


class EditForumComment(TemplateView):
    """ 
    Edit a comment of a selected topic post in the forum
    """

    def get(self, request, pk):
        
        comment = get_object_or_404(ForumPostComment, pk=pk)
        post = comment.post
        form = ForumPostCommentForm(instance=comment)        
        template_name = 'forum/edit_forum_comment.html'
        messages.info(request, f'\
            You are currently editing your comment.')
        context = {
            'post': post,
            'comment': comment,
            'form':form,
            'forum': True,
            'stop_toast_cart': True,
            }
        return render(request, template_name, context)

    def post(self, request, pk):
        comment = get_object_or_404(ForumPostComment, pk=pk)
        pk = comment.post.pk
        form = ForumPostCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.instance.approved = False           
            form.save()
            messages.success(request, f'\
                You have succesfully updated your comment. \
                Your comment has been submitted to admin for\
                     approval and will appear shortly.') 
            
            return HttpResponseRedirect(reverse('post_detail', args=[pk]))

        else:
            messages.error(request, f'\
                Failed to update comment. Please check your data is valid') 
            comment = get_object_or_404(ForumPostComment, pk=pk) 
            post = comment.post      
            form = ForumPostCommentForm(instance=comment)
            messages.info(request, f'You are currently editing your comment.')
            template = 'forum/edit_forum_comment.html'
            context = {
                'post': post,
                'comment': comment,
                'form': form,
                'forum': True,
                'stop_toast_cart': True,
            }
            return render(request, template, context)
  

class DeleteForumComment(TemplateView):
    """
    Delete a selected topic post comment in the forum
    """
    def get(self, request, pk):
               
        comment = get_object_or_404(ForumPostComment, pk=pk)
        post = comment.post
        template_name = 'forum/delete_forum_comment.html'
        messages.info(request, f'\
            You are currently deleting your comment')
        context = {
            'post': post,
            'comment': comment,
            'forum': True,
            'stop_toast_cart': True,
            }
        return render(request, template_name, context)

    def post(self, request, pk):
        comment = get_object_or_404(ForumPostComment, pk=pk)
        pk = comment.post.pk
        comment.delete()
        messages.success(request, '\
            You have successfully deleted the forum comment')
        return HttpResponseRedirect(reverse('post_detail', args=[pk]))

   
class CommentLike(View):
    """
        Class based view to toggle the liked status for
        the selected post and saving to the database.
    """
    def post(self, request, pk):
        """
        POST request for processing the Post liked status
        data passed from the reviews details page and if
        form is valid updates and saves status to database.
        """
        comment = get_object_or_404(ForumPostComment, pk=pk)        
        pk = comment.post.pk
        if comment.likes.filter(id=request.user.id).exists():
            comment.likes.remove(request.user)
            messages.success(request, '\
                You have succesfully un-liked this comment.')
        else:
            comment.likes.add(request.user)
            messages.success(request, '\
                You have succesfully liked this comment.')

        return HttpResponseRedirect(reverse('post_detail', args=[pk]))
