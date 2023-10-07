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
from django.urls import path, re_path, include
from mysite.views import homepage, showpost, about, listing, disp_detail
from mysite.views import ch06_templates_lofi, ch06_templates_sleep, ch06_templates_carlist
from mysite.views import ch07_model_db, ch07_detail
from mysite.views import ch08_form, ch08_delpost, ch08_listing, ch08_post, ch08_contact, ch08_postdb, ch08_bmi
from mysite.views import ch09_test_cookie, ch09_post, ch09_login, ch09_logout, ch09_userinfo, ch09_postDiary, ch09_csvdata, ch09_plotly, ch09_plotly_3D
from mysite.views import ch10_userinfo

admin.site.site_header = "我的私人日誌"
admin.site.site_title = "我的私人日誌"
admin.site.index_title = "我的私人日誌後台"

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

    path('ch06_templates_lofi/', ch06_templates_lofi),
    path('ch06_templates_lofi/<int:tvno>/', ch06_templates_lofi, name = 'lofi-url'),

    path('ch06_templates_sleep/', ch06_templates_sleep),
    path('ch06_templates_sleep/<int:tvno>/', ch06_templates_sleep, name = 'sleep-url'),

    path('ch06_templates_carlist/', ch06_templates_carlist),
    path('ch06_templates_carlist/<int:maker>/', ch06_templates_carlist, name = 'carlist-url'),

    path('ch07_Model_db/', ch07_model_db),
    path('ch07_Model_db/ch07_detail/<int:id>/', ch07_detail, name = 'detail-url'),

    path('ch08_form/', ch08_form),
    path('ch08_delpost/<int:pid>/<str:del_pass>/', ch08_delpost),
    path('ch08_list/', ch08_listing),
    path('ch08_post/', ch08_post),
    path('ch08_contact/', ch08_contact),
    path('ch08_postdb/', ch08_postdb),

    path('captcha/', include('captcha.urls')),

    path('ch08_bmi/', ch08_bmi),

    path('ch09_test_cookie/', ch09_test_cookie),
    path('ch09_post/', ch09_post),
    path('ch09_login/', ch09_login),
    path('ch09_logout/', ch09_logout),
    path('ch09_userinfo/', ch09_userinfo),
    path('ch09_postDiary/', ch09_postDiary),
    path('ch09_csvdata/', ch09_csvdata),
    path('ch09_plotly/', ch09_plotly),
    path('ch09_plotly_3D', ch09_plotly_3D),

    path('accounts/', include('registration.backends.default.urls')),
    path('ch10_userinfo/', ch10_userinfo),
]
