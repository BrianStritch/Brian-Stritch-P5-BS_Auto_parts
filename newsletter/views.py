""" newsletter views.py """
# imports
# 3rd party imports from django
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic import TemplateView

# internal imports from BS_Auto_parts
from .models import Newsletter
from .forms import NewsletterSignupForm


class NewsletterSignup(TemplateView):
    """ class to handle newsletter signup form on index page """

    def post(self, request):
        """ function to handle response from newsletter form """
        form = NewsletterSignupForm(request.POST)
        print(form)  # this will not run with this print statement removed
        if form.instance.optin == 0:
            try:
                try:
                    query = get_object_or_404(Newsletter,
                                              email=form.instance.email)
                except:
                    query.optin = 3
                if query.optin == 0:
                    if query.email == form.instance.email:
                        messages.info(
                            request, '\
                                It appears that you are already opted \
                                    in to our newsletter.')
                        form = NewsletterSignupForm(request.POST)
                        blankform = NewsletterSignupForm()
                        template_name = 'home/index.html'
                        context = {
                            'stop_toast_cart': True,
                            'form': blankform,
                        }
                        return render(request, template_name, context)
                    else:
                        if form.is_valid:
                            form.save()
                            template_name = (
                                'newsletter/newsletter_signup_success.html')
                            messages.success(request, 'Signup Successful')
                            context = {
                                'stop_toast_cart': True,
                            }
                            return render(request, template_name, context)
                        else:
                            messages.error(
                                request,
                                'Your signup was unsuccesful, please try again'
                            )
                            form = NewsletterSignupForm(request.POST)
                            template_name = 'home/index.html'
                            context = {
                                'stop_toast_cart': True,
                                'form': form,
                            }
                            return render(request, template_name, context)
                else:
                    try:
                        email = form.instance.email
                        user = get_object_or_404(Newsletter, email=email)
                        user.optin = 0
                        user.save()
                        template_name = (
                            'newsletter/newsletter_signup_success.html')
                        messages.success(request, 'Status update Successful')
                        context = {
                            'stop_toast_cart': True,
                        }
                        return render(request, template_name, context)
                    except:
                        form.save()
                        template_name = (
                            'newsletter/newsletter_signup_success.html')
                        messages.success(request, 'Signup Successful')
                        context = {
                            'stop_toast_cart': True,
                        }
                        return render(request, template_name, context)

            except:
                if form.is_valid:
                    messages.success(request, 'Your signup was successful')
                    form = NewsletterSignupForm(request.POST)
                    form.save()
                    template_name = 'newsletter/newsletter_signup_success.html'
                    context = {
                        'stop_toast_cart': True,
                    }
                    return render(request, template_name, context)
                else:
                    messages.error(
                        request, '\
                        this is the else of the except not valid')
                    form = NewsletterSignupForm(request.POST)
                    template_name = 'newsletter/newsletter_signup_success.html'
                    context = {
                        'stop_toast_cart': True,
                    }
                    return render(request, template_name, context)

        elif form.instance.optin == 1:
            try:
                queryset = Newsletter.objects.all()
                if queryset.filter(email=form.instance.email).exists():
                    query = get_object_or_404(Newsletter,
                                              email=form.instance.email)

                    if query.email == form.instance.email:
                        email = form.instance.email
                        user = get_object_or_404(Newsletter, email=email)
                        user.optin = 1
                        user.save()
                        template_name = 'newsletter/newsletter_opt_out.html'
                        messages.success(request, 'Opt-out Successful')
                        context = {
                            'stop_toast_cart': True,
                        }
                        return render(request, template_name, context)
                    else:
                        messages.success(
                            request, 'Your signup was successful. if you\
                            wish to optin to the newsletter you can change \
                                your status via the signup section.')
                        form = NewsletterSignupForm(request.POST)
                        form.save()
                        blankform = NewsletterSignupForm()
                        template_name = 'home/index.html'
                        context = {
                            'stop_toast_cart': True,
                            'form': blankform,
                        }
                        return render(request, template_name, context)
                else:
                    messages.success(
                        request, 'Your signup was \
                        successful. if you wish to optin to the \
                        newsletter you can change your status \
                        via the signup section.')
                    form = NewsletterSignupForm(request.POST)
                    form.save()
                    blankform = NewsletterSignupForm()
                    template_name = 'home/index.html'
                    context = {
                        'stop_toast_cart': True,
                        'form': blankform,
                    }
                    return render(request, template_name, context)
            except:
                messages.error(
                    request, '\
                    Your signup was un-successful. Please try again.')
                form = NewsletterSignupForm(request.POST)
                template_name = 'home/index.html'
                context = {
                    'stop_toast_cart': True,
                    'form': form,
                }
                return render(request, template_name, context)

        elif form.instance.optin == 2:
            try:
                queryset = Newsletter.objects.all()
                query = Newsletter.objects.get(email=form.instance.email)
                if query.email == form.instance.email:
                    email = query.email
                    subscriber = get_object_or_404(Newsletter, email=email)
                    subscriber.delete()
                    template_name = 'newsletter/newsletter_removed.html'
                    messages.success(
                        request, 'You have removed your email\
                         from the newsletter database successfully.')
                    context = {
                        'stop_toast_cart': True,
                    }
                    return render(request, template_name, context)
                else:
                    messages.info(
                        request, 'You do not need to withdraw from\
                         our newsletter database as your email\
                             is not stored in our database')
                    blankform = NewsletterSignupForm()
                    template_name = 'home/index.html'
                    context = {
                        'stop_toast_cart': True,
                        'form': blankform,
                    }
                    return render(request, template_name, context)

            except:
                messages.info(
                    request, 'You do not need to withdraw from\
                         our newsletter database as your email is not\
                             stored in our database2')
                form = NewsletterSignupForm()
                template_name = 'home/index.html'
                context = {
                    'stop_toast_cart': True,
                    'form': form,
                }
                return render(request, template_name, context)

        else:
            messages.error(
                request, 'there was a problem with the your data,\
                 please try again.')
            form = NewsletterSignupForm()
            template_name = 'home/index.html'
            context = {
                'stop_toast_cart': True,
                'form': form,
            }
            return render(request, template_name, context)


class NewsletterSubscribers(TemplateView):
    """
    Class based tempate view to render a page displaying all
    newsletter subscribers
    """

    def get(self, request):
        """
        function to return a list of the newsletter
         subscribers and their values
        """
        lists = Newsletter.objects.all()
        template_name = 'newsletter/newsletter_list.html'
        context = {
            'list': lists,
        }
        return render(request, template_name, context)
