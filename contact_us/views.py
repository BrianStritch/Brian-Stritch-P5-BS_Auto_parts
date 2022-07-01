from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import TemplateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib import messages


from .models import ExistingUsersContactDetails, SiteUsersContactDetails
from contact_us.forms import CreateSiteUsersContactDetailsForm , CreateSimpleUsersContactForm , CreateExistingUsersContactForm



class ContactUs(TemplateView):
    def get(self,request):
        form = CreateSiteUsersContactDetailsForm
        template_name = 'contact_us/contact_us.html'
        messages.info(request, 'this is a test message')
        context = {
            'form': form,            
            'stop_toast_cart': True,
            'forum':True,
        }
        return render(request, template_name, context)

    def post(self,request):
        form = CreateSiteUsersContactDetailsForm(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Your message has been succesfully\
                 submitted and Admin will be in contact shortly.')            
            return redirect('home')            
       
        else:
            messages.error(request, 'Failed to send message. Please check your form details.')
            form = CreateSiteUsersContactDetailsForm(request.POST)
            template = 'contact_us/contact_us.html'
            context = {
                'form': form,
                'stop_toast_cart': True,
                'forum':True,
            }
            return render(request, template, context)

        


class SimpleContactUs(TemplateView):
    def get(self,request):
        form = CreateSimpleUsersContactForm
        template_name = 'contact_us/contact_us.html'
        context = {
            'form': form
        }
        return render(request, template_name, context)

    def post(self,request):
        form = CreateSimpleUsersContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Your message has been succesfully\
                 submitted and Admin will be in contact shortly.')            
            return redirect('home')            
       
        else:
            messages.error(request, 'Failed to send message. Please check your form details.')
            form = CreateSimpleUsersContactForm(request.POST)
            template = 'contact_us/contact_us.html'
            context = {
                'form': form,
                'stop_toast_cart': True,
                'forum':True,
            }
            return render(request, template, context)

        


class ExistingUsersContactUs(TemplateView):
    def get(self,request, pk):
        user = get_object_or_404(User, pk=pk)
        form = CreateExistingUsersContactForm
        messages.success(request, 'this is a test message')
        template_name = 'contact_us/contact_us.html'
        context = {
            'form': form,
            'user': user
        }
        return render(request, template_name, context)

    def post(self,request, pk):
        form = CreateExistingUsersContactForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            contact = form.save()
            messages.success(request, 'Your message has been succesfully\
                 submitted and Admin will be in contact shortly.')            
            return redirect('home')            
       
        else:
            messages.error(request, 'Failed to send message. Please check your form details.')
            form = CreateExistingUsersContactForm(request.POST)
            template = 'contact_us/contact_us.html'
            context = {
                'form': form,
                'stop_toast_cart': True,
                'forum':True,
            }
            return render(request, template, context)

        
