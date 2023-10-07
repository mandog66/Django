from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from mysite.models import Post, Product
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
