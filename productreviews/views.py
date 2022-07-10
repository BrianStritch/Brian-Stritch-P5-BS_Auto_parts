""" product reviews views.py """
# imports
# 3rd party imports from django
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import View
from django.template.defaultfilters import slugify
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q


# internal imports from BS_Auto_parts
from products.models import Product
from .models import ProductReview
from .forms import CreateProductReviewForm


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
            summary = form.cleaned_data['summary']
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
            product_review = get_object_or_404(ProductReview, pk=pk)
            product = product_review.product
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
        product_review = get_object_or_404(ProductReview, pk=pk)
        product = product_review.product
        form = CreateProductReviewForm(request.POST, instance=product_review)
        if form.is_valid():
            product_review.status = 0
            form.instance.product = product
            form.instance.author = request.user
            title = form.cleaned_data['title']
            form.instance.slug = slugify(title)
            content = form.cleaned_data['content']
            summary = form.cleaned_data['summary']
            product_review = form.save(commit=False)
            product_review.post = product_review
            product_review.save()
            messages.success(
                request,
                f'Your review has been updated for { product.name },\
                 your review has been re-submitted to administration \
                    for approval.'
                 )
            return HttpResponseRedirect(reverse('products'))
        else:
            form = CreateProductReviewForm()
            messages.error(request, 'your update has failed')
            return render(request, self.template_name, {'form': form})

        return HttpResponseRedirect(reverse('products'))


class DeleteProductReview(TemplateView):
    """
        Class based view to delete the selected
        review.
    """
    def get(self, request, pk):
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
            review = get_object_or_404(ProductReview, pk=pk)
            product = review.product
            if request.user.is_superuser:
                template_name = 'product_reviews/delete_product_review.html'
                messages.info(
                    request,
                    f'You are currently deleting {review.title}'
                    )
                context = {
                    'review': review,
                    'product': product,
                    'stop_toast_cart': True,
                    }
                return render(request, template_name, context)
            else:
                messages.error(
                    request,
                    'Only staff have access to this feature.'
                    )
                return redirect(reverse('home'))

    def post(self, request, pk):
        """ method to handle the post request"""
        if request.user.is_superuser:
            product_review = get_object_or_404(ProductReview, pk=pk)
            product_review.delete()
            pk = product_review.product.id
            messages.success(
                request,
                'You have successfully deleted your review.'
                )
            return redirect(reverse('product_detail', args=[pk]))
        else:
            messages.error(request, 'Only staff have access to this feature.')
            return redirect(reverse('home'))


class ReviewLike(View):
    """
        Class based view to toggle the liked status for
        the selected comment and saving to the database.
    """
    def post(self, request, pk):
        """
        POST request for processing the review liked status
        data passed from the reviews details page and if
        form is valid updates and saves status to database.
        """
        review = get_object_or_404(ProductReview, id=pk)
        pkr = review.product.pk
        if review.likes.filter(id=request.user.id).exists():
            review.likes.remove(request.user)
            messages.success(
                request,
                'You have succesfully un-liked this review.'
                )
        else:
            review.likes.add(request.user)
            messages.success(
                request,
                'You have succesfully liked this review.'
                )

        return HttpResponseRedirect(reverse('product_detail', args=[pkr]))
