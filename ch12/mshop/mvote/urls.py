"""mvote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from mysite import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('paypal/', include("paypal.standard.ipn.urls")),
    path('accounts/', include('allauth.urls')),
    path('', views.index),
    path('<int:id>/', views.index),

    path('filer/', include('filer.urls')),

    path('product/<int:id>/', views.product, name='product-url'),

    path('cart/', views.cart_detial),
    path('cart/additem/<int:id>/<int:quantity>/', views.add_to_cart, name='additem-url'),
    path('cart/removeitem/<int:id>/', views.remove_from_cart, name='removeitem-url'),

    path('order/', views.order),
    path('myorders/', views.my_orders),

    path('payment/<int:id>/', views.payment),
    path('done/', views.payment_done),
    path('canceled/', views.payment_canceled),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
