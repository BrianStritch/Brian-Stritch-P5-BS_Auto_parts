"""
    imports  ------Reviews views.py----------------------
"""
# third party imports
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.template.defaultfilters import slugify
from django.views.generic import TemplateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages

# internal imports
from products.models import Product
from .models import ProductReview, ProductReviewComment
from .forms import ProductReviewCommentForm, CreateProductReviewForm


class CreateProductReview(TemplateView):
    """
        Class based view to render create reviews page
        with CreateProductReviewForm to create new reviews, GET request
        data from user and process POST request accordingly
    """
    template_name = 'product_reviews/create_product_review.html'

    def get(self, request, pk, *args, **kwargs):
        """
        GET request for rendering the create review
        page including the CreateProductReviewForm
        """
        product = get_object_or_404(Product, pk=pk)
        form = CreateProductReviewForm()
        context = {
            'form': form,
            'product': product,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        """
        POST request for processing the CreateProductReviewForm
        data passed from the create review page and if
        form is valid saves booking to database.
        """
        product = get_object_or_404(Product, pk=pk)
        form = CreateProductReviewForm(request.POST)
        if form.is_valid():
            form.instance.product = product
            form.instance.author = request.user
            title = form.cleaned_data['title']
            form.instance.slug = slugify(title)
            content = form.cleaned_data['content']
            excerpt = form.cleaned_data['excerpt']
            product_review = form.save(commit=False)
            product_review.post = product_review
            product_review.save()
        else:
            form = CreateProductReviewForm()
            return render(request, self.template_name, {'form': form})

        return HttpResponseRedirect(reverse('products'))


class EditProductReview(TemplateView):

    """
        Class based view to display edit product review
        page with createproductreview form relative to the
        current selected product review and for saving
        updated data to the database.
    """
        
    template_name = 'product_reviews/edit_product_review.html'

    def get(self, request, pk, *args, **kwargs):
        product_review = get_object_or_404(ProductReview, product=pk)
        product = get_object_or_404(Product, pk=pk)
        form = CreateProductReviewForm(instance=product_review)
        
        context = {
            'form': form,
            'product': product,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, pk):
        """
        POST request for processing the CreateProductReviewForm
        data passed from the create product review page and if
        form is valid saves booking to database.
        """
        product = get_object_or_404(Product, pk=pk)
        product_review = get_object_or_404(ProductReview, product=pk)
        form = CreateProductReviewForm(request.POST, instance=product_review)
        if form.is_valid():
            product_review.status=0
            form.instance.product = product
            form.instance.author = request.user
            title = form.cleaned_data['title']
            form.instance.slug = slugify(title)
            content = form.cleaned_data['content']
            excerpt = form.cleaned_data['excerpt']
            product_review = form.save(commit=False)
            product_review.post = product_review
            product_review.save()
            messages.success(request, f'Your review has been updated for { product.name },\
                 your review has been re-submitted to administration for approval.')
            return HttpResponseRedirect(reverse('products'))
        else:
            form = CreateProductReviewForm()
            messages.error(request, 'your update has failed')
            return render(request, self.template_name, {'form': form})

        return HttpResponseRedirect(reverse('products'))


class DeleteProductReview(DeleteView):
    """
        Class based view to delete the selected
        review using the built in Django Deleteview.
    """
    model = ProductReview
    template_name = 'product_reviews/delete_product_review.html'
    success_url = reverse_lazy('products')

###############################  Reviews Comments  ####################################################
class ReviewsComments(View):
    """
        Class based view to display the selected
        reviews specific details and comments.
    """
    template_name = "product_reviews/create_product_review_comment.html"

    def get(self, request, slug):
        """
        class based function to render the reviews detail page
        diaplaying the review details for the selected review
        and renders the commentform and displays all comments
        related to the specific review.
        """
        form = ProductReviewCommentForm()
        queryset = ProductReview.objects.filter(status=1) 
        review = get_object_or_404(queryset, slug=slug) 
        comments = review.product_review_comments.filter(approved=True).order_by('created_on') 
        liked = False

        
        
        if review.likes.filter(id=request.user.id).exists():
            liked = True
            try:
                comments = review.comments.filter(approved=True).order_by('created_on')
            except:
                comments = None
            liked = False
            if review.likes.filter(id=self.request.user.id).exists():
                liked = True

        return render(
            request,
            self.template_name,
            {
                "review": review,
                "comments": comments,
                "commented": False,
                "liked": liked,
                'form': form,

            },
        )

    def post(self, request, slug):
        """
        POST request for processing the CommentForm
        data passed from the reviews details page and if
        form is valid saves comment to database.
        """
        products = Product.objects.all()
        queryset = ProductReview.objects.filter(status=1) 
        review = get_object_or_404(queryset, slug=slug) 
        comments = review.product_review_comments.filter(approved=True).order_by('created_on')
        liked = False
        try:
            comments = review.comments.filter(approved=True).order_by('created_on')
        except:
            comments = None
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        form = ProductReviewCommentForm(data=request.POST)

        if  form.is_valid():
            form.instance.email = request.user.email
            form.instance.name = request.user.username
            comment = form.save(commit=False)
            comment.product_review = review
            comment.save()
            messages.success(request, 'Your comment has been created \
                succesfully and is pending approval and will appear shortly.') 

        else:
            form = ProductReviewCommentForm()
            messages.error(request, 'Your comment has not been created, please check \
                your form data and re submit.')
        
        template_name = 'products/products.html'


        return render(
            request,
            template_name,
            {
                "review": review,
                "comments": comments,
                "commented": True,
                "liked": liked,
                'form': form,
                'products':products
            },
        )


class EditComment(TemplateView):
    """
        Class based view to display edit comment
        page with comment form relative to the
        current selected review and utilising
        the built in django updateview for saving
        updated data to the database.
    """

    """
        Class based view to display edit product review
        page with createproductreview form relative to the
        current selected product review and for saving
        updated data to the database.
    """
        
    template_name = 'product_reviews/edit_product_review_comment.html'

    def get(self, request, pk, *args, **kwargs):
    
        comment = get_object_or_404(ProductReviewComment, pk=pk)
        form = ProductReviewCommentForm(instance=comment)
        template_name = 'product_reviews/edit_product_review_comment.html'
        context = {
            'form': form,
            'comment': comment,
        }
        return render(request, template_name, context)
    
    def post(self, request, pk):
        """
        POST request for processing the CreateProductReviewForm
        data passed from the create product review page and if
        form is valid saves booking to database.
        """
        comment = get_object_or_404(ProductReviewComment, pk=pk)
        form = ProductReviewCommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment.approved=False
            form.instance.body = form.cleaned_data['body']            
            form.save()
            messages.success(request, f'Your comment has been updated and,\
                 your review has been re-submitted to administration for approval.')
            return HttpResponseRedirect(reverse('products'))
        else:
            form = ProductReviewCommentForm()
            messages.error(request, 'your update has failed')
            return render(request, self.template_name, {'form': form})

        return HttpResponseRedirect(reverse('products'))


class DeleteComment(DeleteView):
    """
        Class based view to delete the selected
        comment using the built in Django Deleteview.
    """
    model = ProductReviewComment
    template_name = 'product_reviews/delete_product_review_comment.html'
    success_url = reverse_lazy('products')


class ReviewLike(View):
    """
        Class based view to toggle the liked status for
        the selected comment and saving to the database.
    """
    def post(self, request, slug):
        """
        POST request for processing the review liked status
        data passed from the reviews details page and if
        form is valid updates and saves status to database.
        """
        post = get_object_or_404(Review, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('review_details', args=[slug]))

##################################################################################################

