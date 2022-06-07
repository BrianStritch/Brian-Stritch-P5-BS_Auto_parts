from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """
    A view to display a users profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully')

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        }

    return render(request, template, context)
