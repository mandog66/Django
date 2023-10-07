from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from mysite.models import Post, Product, Ch07_Product, PPhoto
from datetime import datetime
import random

quotes = ['今日事，今日畢',
        '要怎麼收穫，先那麼栽',
        '知識就是力量',
        '一個人的個性就是他的命運']

# 取得資料庫中所有紀錄
def homepage(request):
    # posts = Post.objects.all()
    # post_lists = list()
    # for count, post in enumerate(posts):
    #     post_lists.append("No. {}:".format(str(count)) + str(post) + "<hr>")
    #     post_lists.append("<small>" + str(post.body) + "</small><br><br>")

    # return HttpResponse(post_lists)

    # 網頁輸出模板templates
    posts = Post.objects.all()
    now = datetime.now()

    quote = random.choice(quotes)

    return render(request, "index.html", locals())

# 顯示單篇文章
def showpost(request, slug):
    try:
        post = Post.objects.get(slug = slug)
        if post != None:
            quote = random.choice(quotes)
            return render(request, 'post.html', locals())
    except:
        return redirect('/')
    
def about(request):
    return render(request, 'about.html', locals())

def listing(request):
    products = Product.objects.all()
    return render(request, 'list.html', locals())

def disp_detail(request, sku):
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的品項編號')
    return render(request, 'disp.html', locals())

def ch06_templates_lofi(request, tvno = 0):
    tv_list = [{'name':'Lofi Girl', 'tvcode':'jfKfPfyJRdk'},
               {'name':'Lofi Boy', 'tvcode':'4xDzrJKXOOY'}]
    now = datetime.now()
    tv = tv_list[tvno]
    quote = random.choice(quotes)
    return render(request, 'ch06_templates_lofi.html', locals())

def ch06_templates_sleep(request, tvno = 0):
    tv_list = [{'name':'Lofi Girl', 'tvcode':'jfKfPfyJRdk'},
               {'name':'Lofi Boy', 'tvcode':'4xDzrJKXOOY'},
               {'name':'Sleep', 'tvcode':'rUxyKA_-grg'},]
    now = datetime.now()
    tv = tv_list[tvno]
    quote = random.choice(quotes)
    return render(request, 'ch06_templates_sleep.html', locals())

def ch06_templates_carlist(request, maker = 0):
    car_maker = ['SAAB', 'Ford', 'Honda', 'Mazda', 'Nissan','Toyota' ]
    car_list = [ [],
            [{'model':'Fiesta', 'price':100}, 
             {'model':'Focus', 'price':200}, 
             {'model':'Modeo', 'price':300}, 
             {'model':'EcoSport', 'price':400}, 
             {'model':'Kuga', 'price':500}, 
             {'model':'Mustang', 'price':600}],
            [{'model':'Fit', 'price':700}, 
             {'model':'Odyssey', 'price':800}, 
             {'model':'CR-V', 'price':900}, 
             {'model':'City', 'price':1000}, 
             {'model':'NSX', 'price':1100}],
            [{'model':'Mazda3', 'price':1200}, 
             {'model':'Mazda5', 'price':1300}, 
             {'model':'Mazda6', 'price':1400}, 
             {'model':'CX-3', 'price':1500}, 
             {'model':'CX-5', 'price':1600}, 
             {'model':'MX-5', 'price':1700}],
            [{'model':'Tida', 'price':1800}, 
             {'model':'March', 'price':1900}, 
             {'model':'Livina', 'price':2000}, 
             {'model':'Sentra', 'price':3000}, 
             {'model':'Teana', 'price':4000}, 
             {'model':'X-Trail', 'price':5000}, 
             {'model':'Juke', 'price':6000}, 
             {'model':'Murano', 'price':7000}],
            [{'model':'Camry', 'price':8000},
             {'model':'Altis', 'price':9000},
             {'model':'Yaris', 'price':10000},
             {'model':'86', 'price':11000},
             {'model':'Prius', 'price':12000},
             {'model':'Vios', 'price':13000}, 
             {'model':'RAV4', 'price':14000}, 
             {'model':'Wish', 'price':15000}]
              ]
    maker_name = car_maker[maker]
    cars = car_list[maker]
    return render(request, 'ch06_templates_carlist.html', locals())

def ch07_model_db(request):
    products = Ch07_Product.objects.all()

    quote = random.choice(quotes)
    
    return render(request, 'ch07_model_db.html', locals())

def ch07_detail(requset, id):
    try:
        quote = random.choice(quotes)
        product = Ch07_Product.objects.get(id=id)
        images = PPhoto.objects.filter(product=product)
    except:
        pass
    return render(requset, 'ch07_detail.html', locals())
