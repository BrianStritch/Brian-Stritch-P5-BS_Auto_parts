# imports
# 3rd party imports from django
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import TemplateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import UserProfile
from django.db.models import Q

# internal imports from BS_Auto_parts
from .forms import UserAccountDetailsForm, UserProfileForm, EditProfileForm
from django.contrib.auth.forms import UserCreationForm
from checkout.models import Order
from products.models import Product



class SignUp(TemplateView):
    """
    SIgn Up template with form which allows users to input a username,
    first name, last name, email address and a password with a password
    verifcation check.
    """
    template_name = 'profiles/sign_up.html'

    def get(self, request, *args, **kwargs):
        """
        GET request for rendering the sign up
        page including the User account details form
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
            form = UserCreationForm()
            return render(
                request,
                self.template_name,
                {
                    'form': form,
                })

    def post(self, request):
        """
        POST request for processing the User account details form
        data passed from thesign up page and if
        form is valid saves user to database.
        """
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('home'))

            else:
                form = UserCreationForm()
                context = {
                    'form': form,
                }
                return render(request, self.template_name, context)

        else:
            form = UserCreationForm()
            context = {
                'form': form,
            }
            return render(request, self.template_name, context)


@login_required
def profile(request):
    """
    A view to display a users profile
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
        profile = get_object_or_404(UserProfile, user=request.user)
        

        if request.method == 'POST':
            form = UserProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your profile has been updated successfully')
            else:
                messages.error(request, 'Update failed. Please ensure form data is correct.')
        else:
            form = UserProfileForm(instance=profile)

        orders = profile.orders.all()

        template = 'profiles/profile.html'
        context = {
            'profile': profile,
            'form': form,
            'orders': orders,
            'stop_toast_cart': True,
            }

        return render(request, template, context)


@login_required
def order_history(request, order_number):
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
        order = get_object_or_404(Order, order_number=order_number)

        messages.info(
            request,(
            f'This is a past confirmation for order number { order_number }. '
                'A confirmation email was sent on the order date.' 
            ))

        template = 'checkout/checkout_success.html'
        context = {
            'order': order,
            'from_profile': True,
        }

        return render(request, template, context)


class EditProfile(TemplateView):
    """
    Class based view which renders the edit profile template with form
    which allows users to Edit their username,
    first name, last name, email address and a password with a password
    verifcation check.
    """
    template_name = 'profiles/edit_profile.html'

    def get(self, request, *args, **kwargs):
        """
        GET request for rendering the edit user profile
        page including the edit profile form
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
            person = User.objects.get(pk=request.user.id)
            form = EditProfileForm(instance=person)
            context = {
                    'form': form,
                    'person': person,
                }
            return render(request, self.template_name, context)

    def post(self, request):
        """
        POST request for processing the edit profile form
        data passed from edit profile page and if
        form is valid updates and saves user data to database.
        """
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile details updated successfully.')
                return HttpResponseRedirect(reverse('profile'))

            else:
                form = EditProfileForm(instance=request.user)
                context = {
                    'form': form,
                }
                messages.error(request, 'Update unsuccesful. Please check your form details are correct.')
                return render(request, self.template_name, context)

        else:
            form = EditProfileForm(instance=request.user)
            context = {
                'form': form,
            }
            return render(request, self.template_name, context)


class DeleteProfile(TemplateView):
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
                return redirect(reverse('home'))

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
            user = get_object_or_404(User, pk=pk)
            if request.user == user:        
                template_name = 'profiles/delete_profile.html'
                messages.info(request, f'You are currently deleting profile for {user.username}')
                context = {
                    'stop_toast_cart': True,
                    }
                return render(request, template_name, context)
            else:
                messages.error(request, 'Only the User can have access to this feature.') 
                return redirect(reverse('home'))

    def post(self, request, pk): 
        user = get_object_or_404(User, pk=pk)
        if request.user == user: 
          user.delete()
          messages.success(request, 'You have successfully deleted your Account.')
          return redirect(reverse('home'))    
          
        else:
            messages.error(request, 'Only the User can have access to this feature.') 
            return redirect(reverse('home'))
        
