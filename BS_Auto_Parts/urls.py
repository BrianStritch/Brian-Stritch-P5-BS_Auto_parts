"""BS_Auto_Parts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('product_review/', include('productreviews.urls')),
    path('forum/', include('forum.urls')),
    path('favourites/', include('favourites.urls')),
    path('contact_us/', include('contact_us.urls')),
    path('staff/', include('storeowners.urls')),
    path('newsletter/', include('newsletter.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'BS_Auto_Parts.views.handler404'
handler400 = 'BS_Auto_Parts.views.handler400'
handler401 = 'BS_Auto_Parts.views.handler401'
handler500 = 'BS_Auto_Parts.views.handler500'
