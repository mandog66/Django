#-*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token, csrf_protect
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
from allauth.account.decorators import verified_email_required
from mysite import models, forms
from cart.cart import Cart

# Create your views here.

def index(request, id=0):
    try:
        all_products = None
        all_categories = models.Category.objects.all().order_by('name')

        if id > 0:
            category = models.Category.objects.get(id=id)
            if category is not None:
                all_products = models.Product.objects.filter(category=category)
        if all_products is None:
            all_products = models.Product.objects.all().order_by('name')
        paginator = Paginator(all_products, 4)
        p = request.GET.get('p')
        products = paginator.page(p)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    except Exception:
        products = []
    
    all_categories = models.Category.objects.all().order_by('name')

    return render(request, 'index.html', locals())

def product(request, id):
    all_categories = models.Category.objects.all().order_by('name')
    try:
        product = models.Product.objects.get(id=id)
    except:
        product = None
    
    return render(request, 'product.html', locals())

@login_required
def add_to_cart(request, id, quantity):
    cart = Cart(request)
    product = models.Product.objects.get(id=id)

    if cart.cart and str(id) in cart.cart.keys():
        if (int(cart.cart[str(id)]['quantity']) + quantity) > int(product.stock):
            messages.add_message(request, messages.WARNING, "庫存不足")
            # return render(request, 'index.html', locals())
            return redirect('/')
        else:
            cart.add(product=product, quantity=quantity)
            return redirect('/')
    else:
        cart.add(product=product, quantity=quantity)
        return redirect('/')


    # print('##################################')
    # if cart.cart:
    #     print(cart.cart.keys())
    # else:
    #     print('None')
    # print('##################################')
    # print(cart.cart.items())
    # print('##################################')
    # print(cart.cart)
    # print('##################################')
    # print(cart.cart.keys())
    # print('##################################')
    # print('4' in cart.cart.keys())
    # if cart.request.GET.get('id'):
    #     print('##################################')
    #     print(cart.cart.items())
    #     print('##################################')
    #     print((int(cart.cart[str(id)]['quantity']) + quantity))
    #     print('##################################')
    #     print(product.stock)

    #     if (int(cart.cart[str(id)]['quantity']) + quantity) > int(product.stock):
    #         messages.add_message(request, messages.WARNING, "庫存不足")
    #         return render(request, 'index.html', locals())

@login_required
def remove_from_cart(request, id):
    cart = Cart(request)
    product = models.Product.objects.get(id=id)
    cart.remove(product)
    
    return redirect('/cart/')

@login_required
def cart_detial(request):
    all_categories = models.Category.objects.all().order_by('name')
    cart = Cart(request).cart

    total_price = 0
    for _, item in cart.items():
        current_price = float(item['price']) * int(item['quantity'])
        total_price += current_price
    
    return render(request, 'cart.html', locals())

@verified_email_required
def order(request):
    all_categories = models.Category.objects.all()
    cartInstance = Cart(request)
    cart = cartInstance.cart
    total_price = 0
    for _, item in cart.items():
        current_price = float(item['price']) * int(item['quantity'])
        total_price += current_price
    
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        new_order = models.Order(user=user)

        form = forms.OrderForm(request.POST, instance=new_order)
        if form.is_valid():
            order = form.save()
            email_messages = "您的購物內容如下 : \n"
            for _, item in cart.items():
                product = models.Product.objects.get(id=item['product_id'])
                models.OrderItem.objects.create(
                    order = order,
                    product = product,
                    price = item['price'],
                    quantity = item['quantity']
                )
                email_messages = email_messages + "\n" + \
                                 "{}, {}, {}".format(item['name'], \
                                                     item['price'], item['quantity'])
            # "標點符號要全形"
            email_messages = email_messages + "\n以上共計{}元\nhttp://mshop.hhg.com感謝您的訂購。".format(total_price)
            cartInstance.clear()
            messages.add_message(request, messages.INFO, "訂單已儲存，我們會盡快處理。")
            email = EmailMessage("感謝您的訂購", email_messages, "迷你小店商<admin@admin.com>", [request.user.email])
            email.send()
            email = EmailMessage("有人訂購產品囉", email_messages, "迷你小店商<admin@admin.com>", ['tiger871014@gmail.com'])
            email.send()
            return redirect("/myorders/")
        else:
            form = forms.OrderForm()
        
    return render(request, 'order.html', locals())
    
@login_required
def my_orders(request):
    all_categories = models.Category.objects.all()
    orders = models.Order.objects.filter(user=request.user)
    return render(request, 'myorders.html', locals())

@csrf_exempt
def payment_done(request):
    all_categories = models.Category.objects.all()
    return render(request, 'payment_done.html', locals())

@csrf_exempt
def payment_canceled(request):
    all_categories = models.Category.objects.all()
    return render(request, 'payment_canceled.html', locals())

@csrf_protect
def payment(request, id):
    try:
        all_categories = models.Category.objects.all()
        order = models.Order.objects.get(id=id)
        all_order_items = models.OrderItem.objects.filter(order=order)
        items = list()
        total = 0
        for order_item in all_order_items:
            t = dict()
            t['name'] = order_item.product.name
            t['price'] = order_item.product.price
            t['quantity'] = order_item.quantity
            t['subtotal'] = order_item.product.price * order_item.quantity
            total = total + order_item.product.price
            items.append(t)
        host = request.get_host()
        # 注意最後也要加上逗點
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": total,
            "item_name": "迷你小電商貨品編號：{}".format(id),
            "invoice": "invoice-{}".format(id),
            "currency_code": "TWD",
            # "notify_url": "http://{}{}".format(host, reverse('paypal-ipn')),
            # "return_url": "http://{}/done/".format(host),
            # "cancel_return": "http://{}/canceled/".format(host),

            "notify_url": "http://{}{}".format(host, reverse('paypal-ipn')),
            "return_url": "http://{}/done/".format(host),
            "cancel_return": "http://{}/canceled/".format(host),
        }
        print("############################################")
        print("notify_url : ", end='')
        print(paypal_dict['notify_url'])
        print("############################################")
        print("############################################")
        print("paypal-ipn : ", end='')
        print(reverse('paypal-ipn'))
        print("############################################")
        paypal_form = PayPalPaymentsForm(initial=paypal_dict)
        # order.paid = True
        # order.save()
        return render(request, 'payment.html', locals())
    except:
        messages.add_message(request, messages.WARNING, "訂單編號錯誤，無法處理付款。")
        return redirect('/myorders/')
