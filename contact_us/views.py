from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import TemplateView, UpdateView, DeleteView
from django.contrib.auth.models import User

from .models import ExistingUsersContactDetails, SiteUsersContactDetails
from contact_us.forms import CreateSiteUsersContactDetailsForm , CreateSimpleUsersContactForm , CreateExistingUsersContactForm



class ContactUs(TemplateView):
    def get(self,request):
        form = CreateSiteUsersContactDetailsForm
        template_name = 'contact_us/contact_us.html'
        context = {
            'form': form
        }
        return render(request, template_name, context)

    def post(self,request):

        return redirect('home')


class SimpleContactUs(TemplateView):
    def get(self,request):
        form = CreateSimpleUsersContactForm
        template_name = 'contact_us/contact_us.html'
        context = {
            'form': form
        }
        return render(request, template_name, context)

    def post(self,request):

        return redirect('home')


class ExistingUsersContactUs(TemplateView):
    def get(self,request, pk):
        user = get_object_or_404(User, pk=pk)
        form = CreateExistingUsersContactForm
        template_name = 'contact_us/contact_us.html'
        context = {
            'form': form,
            'user': user
        }
        return render(request, template_name, context)

    def post(self,request):

        return redirect('home')
