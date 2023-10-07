"""mblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from mysite.views import homepage, showpost, about, listing, disp_detail

urlpatterns = [
    # re_path(r'^$', homepage),
    path('', homepage), 

    # re_path('^past/(?P<slug>\d{1, 4})/$', showpost),
    path('post/<slug:slug>/', showpost), 

    # re_path('^about/$, about),
    path('about/', about),

    # re_path('^list/$, listing),
    path('list/', listing),

    # re_path('^list/(?P<sku>\d{1,4})/$, disp_detail),
    path('list/<str:sku>/', disp_detail),

    # re_path('^admin/$, include(admin.site.urls)),
    path('admin/', admin.site.urls),
]
