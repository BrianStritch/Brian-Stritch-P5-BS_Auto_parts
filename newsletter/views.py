from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView, UpdateView, DeleteView
from django.views import generic, View
from django.http import HttpResponseRedirect

from .models import Newsletter
from .forms import NewsletterSignupForm



class NewsletterSignup(TemplateView):
    def post(self, request):
        form = NewsletterSignupForm(request.POST)
        print('form = ', form)
        print('optin = ',form.instance.optin)
        if form.instance.optin == 0 :
            try:
                try:
                    query = get_object_or_404(Newsletter, email=form.instance.email)
                except:
                    query.optin=3
                if query.optin == 0:
                    if query.email == form.instance.email:
                        messages.error(request, 'It appears that you are already opted in to our newsletter.')
                        form = NewsletterSignupForm(request.POST)
                        blankform = NewsletterSignupForm()
                        template_name = 'home/home.html'
                        context = {
                        'stop_toast_cart': True,
                        'form': blankform,

                        }
                        return render(request, template_name, context)
                    else:
                        if form.is_valid:
                            form.save()
                            template_name = 'newsletter/newsletter_signup_success.html'
                            messages.success(request, 'Signup Successful')
                            context = {
                            'stop_toast_cart': True,

                            }
                            return render(request, template_name, context)
                        else:
                            messages.error(request, 'Your signup was unsuccessful, please try again.')
                            form = NewsletterSignupForm(request.POST)
                            template_name = 'home/home.html'
                            context = {
                            'stop_toast_cart': True,
                            'form': form,
                            }
                            return render(request, template_name, context)
                else:
                    try:
                        email = form.instance.email
                        user = get_object_or_404(Newsletter, email=email)                  
                        user.optin=0
                        user.save()
                        template_name = 'newsletter/newsletter_signup_success.html'
                        messages.success(request, 'Status update Successful')
                        context = {
                        'stop_toast_cart': True,
                        }
                        return render(request, template_name, context)
                    except:
                        form.save()
                        template_name = 'newsletter/newsletter_signup_success.html'
                        messages.success(request, 'Signup Successful')
                        context = {
                        'stop_toast_cart': True,
                        }
                        return render(request, template_name, context)
                
            except:
                print('inside except new user')
                messages.error(request, 'Your signup was successful')
                form = NewsletterSignupForm(request.POST)
                form.save()
                template_name = 'newsletter/newsletter_signup_success.html'
                context = {
                'stop_toast_cart': True,
                }
                return render(request, template_name, context)

        elif form.instance.optin == 1:
            try:
                queryset = Newsletter.objects.all()
                if queryset.filter(email=form.instance.email).exists():
                    query = get_object_or_404(Newsletter, email=form.instance.email)
            
                    if query.email == form.instance.email:
                        email = form.instance.email
                        user = get_object_or_404(Newsletter, email=email)
                        user.optin=1
                        user.save()
                        template_name = 'newsletter/newsletter_opt_out.html'
                        messages.success(request, 'Opt-out Successful')
                        context = {
                        'stop_toast_cart': True,
                        }
                        return render(request, template_name, context)
                    else:
                        print('inside except new user')
                        messages.error(request, 'Your signup was successful. if you\
                            wish to optin to the newsletter you can change your status via the signup section.')
                        form = NewsletterSignupForm(request.POST)
                        form.save()
                        blankform = NewsletterSignupForm()
                        template_name = 'home/home.html'
                        context = {
                        'stop_toast_cart': True,
                        'form': blankform,
                        }
                        return render(request, template_name, context)
                else:
                    print('inside except new user')
                    messages.error(request, 'Your signup was successful. if you\
                        wish to optin to the newsletter you can change your status via the signup section.')
                    form = NewsletterSignupForm(request.POST)
                    form.save()
                    blankform = NewsletterSignupForm()
                    template_name = 'home/home.html'
                    context = {
                    'stop_toast_cart': True,
                    'form': blankform,
                    }
                    return render(request, template_name, context)
            except:
                print('inside except new user2')
                messages.error(request, 'Your signup was un-successful. Please try again.')
                form = NewsletterSignupForm(request.POST)
                template_name = 'home/home.html'
                context = {
                'stop_toast_cart': True,
                'form': form,
                }
                return render(request, template_name, context)
                
        elif form.instance.optin == 2:
            email = form.instance.email
            user = get_object_or_404(Newsletter, email=email)            
            user.delete()
            template_name = 'newsletter/newsletter_removed.html'
            messages.success(request, 'You have removed your email from the newsletter database successfully.')
            context = {
            'stop_toast_cart': True,
            }
            return render(request, template_name, context)
            
                