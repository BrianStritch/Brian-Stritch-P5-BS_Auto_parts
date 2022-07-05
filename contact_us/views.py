# imports
# 3rd party imports from django
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import TemplateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib import messages

# internal imports from BS_Auto_parts
from .models import ExistingUsersContactDetails, SiteUsersContactDetails
from contact_us.forms import CreateSiteUsersContactDetailsForm , CreateSimpleUsersContactForm , CreateExistingUsersContactForm



class ContactUs(TemplateView):
    """
    A view to render the contact us page and form and
    a post method to process the data from the form and
    return the user to the home landing page. This class is
    used where a user is not authenticated.
    """
    def get(self,request):
        """
        a get method to render the template passing the 
        CreateSiteUsersContactDetailsForm as context
        """
        form = CreateSiteUsersContactDetailsForm
        template_name = 'contact_us/contact_us.html'
        context = {
            'form': form,            
            'stop_toast_cart': True,
            'forum':True,
        }
        return render(request, template_name, context)

    def post(self,request):
        """
        a method to render  the POST data of the 
        CreateSiteUsersContactDetailsForm passed from the template
        """
        form = CreateSiteUsersContactDetailsForm(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Your message has been succesfully\
                 submitted and Admin will be in contact shortly.')            
            template_name = 'home/home.html' 
            context = {
                'stop_toast_cart': True,
                'home': True,
                'bttoff':True

            } 
            return render(request, template_name, context)             
       
        else:
            messages.error(request, '\
                Failed to send message. Please check your form details.')
            form = CreateSiteUsersContactDetailsForm(request.POST)
            template = 'contact_us/contact_us.html'
            context = {
                'form': form,
                'stop_toast_cart': True,
                'forum':True,
            }
            return render(request, template, context)

        


class SimpleContactUs(TemplateView):
    """
    A view to render the contact us page and form and
    a post method to process the data from the form and
    return the user to the home landing page.
    """
    def get(self,request):
        """
        a method to render the template passing the 
        CreateSimpleUsersContactForm as context
        """
        form = CreateSimpleUsersContactForm
        template_name = 'contact_us/contact_us.html'
        context = {
            'form': form,
            'stop_toast_cart': True,
        }
        return render(request, template_name, context)

    def post(self,request):
        """
        a method to process the POST data of the 
        CreateSimpleUsersContactForm passed from the template
        """
        form = CreateSimpleUsersContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Your message has been succesfully\
                 submitted and Admin will be in contact shortly.') 
            template_name = 'home/home.html' 
            context = {
                'stop_toast_cart': True,
                'home': True,
                'bttoff':True

            } 
            return render(request, template_name, context)         
                        
       
        else:
            messages.error(request, 'Failed to send message.\
                 Please check your form details.')
            form = CreateSimpleUsersContactForm(request.POST)
            template = 'contact_us/contact_us.html'
            context = {
                'form': form,
                'stop_toast_cart': True,
                'forum':True,
            }
            return render(request, template, context)

        


class ExistingUsersContactUs(TemplateView):
    """
    A view to render the contact us page and form and
    a post method to process the data from the form and
    return the user to the home landing page. This class is
    used where a user is authenticated.
    """
    def get(self,request, pk):
        """
        a method to render the template passing the 
        CreateExistingUsersContactForm as context taking the
         user.pk parameter to associate the contact form with
          the relevant user
        """
        user = get_object_or_404(User, pk=pk)
        form = CreateExistingUsersContactForm
        template_name = 'contact_us/contact_us.html'
        context = {
            'form': form,
            'user': user,
            'stop_toast_cart': True,

        }
        return render(request, template_name, context)

    def post(self,request, pk):
        """
        a method to process the POST data of the 
        CreateSiteUsersContactDetailsForm passed from the template
        """
        form = CreateExistingUsersContactForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            contact = form.save()
            messages.success(request, 'Your message has been succesfully\
                 submitted and Admin will be in contact shortly.')            
            template_name = 'home/home.html' 
            context = {
                'stop_toast_cart': True,
                'home': True,
                'bttoff':True

            } 
            return render(request, template_name, context)             
       
        else:
            messages.error(request, 'Failed to send message.\
                 Please check your form details.')
            form = CreateExistingUsersContactForm(request.POST)
            template = 'contact_us/contact_us.html'
            context = {
                'form': form,
                'stop_toast_cart': True,
                'forum':True,
            }
            return render(request, template, context)
