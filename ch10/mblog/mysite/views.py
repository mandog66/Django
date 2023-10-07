from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages, auth
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from mysite.models import Post, Product, Ch07_Product, PPhoto
from mysite.models import ch08_Post, ch08_Mood
from mysite.models import ch09_User, ch09_Profile, ch09_Diary, csv_data
from mysite import forms
from datetime import datetime
from plotly.offline import plot
import plotly.graph_objs as go
import numpy as np
import random, json, urllib, pymongo, os


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

def ch07_detail(request, id):
    try:
        quote = random.choice(quotes)
        product = Ch07_Product.objects.get(id=id)
        images = PPhoto.objects.filter(product=product)
    except:
        pass
    return render(request, 'ch07_detail.html', locals())

def ch08_form(request):
    try:
        quote = random.choice(quotes)
        urid = request.GET['user_id']
        urpass = request.GET['user_pass']
        byear = request.GET['byear']
        urfcolor = request.GET.getlist('fcolor')
    except:
        urid = None

    if urid != None and urpass == "123":
        verified = True
    else:
        verified = False
    years = range(1960, 2024)
    return render(request, 'ch08_form.html', locals())

def ch08_post(request):
    moods = ch08_Mood.objects.all()
    quote = random.choice(quotes)
    message = '如要張貼訊息，則每一個欄位都要填...'

    if request.method == "GET":
        try:
            user_id = request.GET['user_id']
            user_pass = request.GET['user_pass']
            user_post = request.GET['user_post']
            user_mood = request.GET['mood']
        except:
            user_id = None
            message = message

    if request.method == "POST":
        try:
            user_id = request.POST.get('user_id')
            user_pass = request.POST.get('user_pass')
            user_post = request.POST.get('user_post')
            user_mood = request.POST.get('mood')
            if user_id != None:
                mood = ch08_Mood.objects.get(status=user_mood)
                post = ch08_Post(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post, enabled=True)
                post.save()
                return redirect('/ch08_list/')
        except:
            user_id = None
            message = message
    return render(request, 'ch08_post.html', locals())

def ch08_delpost(request, pid = None, del_pass = None):
    if del_pass and pid:
        try:
            post = Post.objects.get(id=pid)
            if post.del_pass == del_pass:
                post.delete()
        except:
            pass
    return redirect('/ch08_list/')

def ch08_listing(request):
    posts = ch08_Post.objects.filter(enabled=True).order_by('pub_time')[:150]
    moods = ch08_Mood.objects.all()
    quote = random.choice(quotes)
    return render(request, 'ch08_list.html', locals())

def ch08_contact(request):
    quote = random.choice(quotes)
    form = forms.ContactForm()

    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            message = "感謝您的來信，我們會儘速處理您的寶貴意見。"
            user_name = form.cleaned_data['user_name']
            user_city = form.cleaned_data['user_city']
            user_school = form.cleaned_data['user_school']
            user_email  = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']

            mail_body = u'''
網友姓名：{}
居住城市：{}
是否在學：{}
電子郵件：{}
反應意見：如下
{}'''.format(user_name, user_city, user_school, user_email, user_message)

            email = EmailMessage(   '來自Mysite網站的意見', 
                                    mail_body, 
                                    user_email,
                                    ['tiger871014@gmail.com'])
            email.send()

        else:
            message = "請檢查您輸入的資訊是否正確！"
    else:
        form = forms.ContactForm()
    return render(request, 'ch08_contact.html', locals())

def ch08_postdb(request):
    quote = random.choice(quotes)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret':settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response':recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            if result['success']:
                post_form.save()
                return redirect('/ch08_list/')
            else:
                message = "請檢查您輸入的資訊是否正確！"
        else:
            message = "請檢查您輸入的資訊是否正確！"
    else:
        post_form = forms.PostForm()
        message = "請檢查您輸入的資訊是否正確！!"

    return render(request, 'ch08_postdb.html', locals())

def ch08_bmi(request):
    quote = random.choice(quotes)
    client = pymongo.MongoClient('mongodb://root:example@mongo:27017/')
    collections = client['ch08']['bodyinfo']
    if request.method == "POST":
        print(request.POST.get("height").isdecimal())
        print(request.POST.get("weight").isdecimal())
        if request.POST.get("height").isdecimal() and request.POST.get("weight").isdecimal():
            name = request.POST.get("name").strip()
            height = request.POST.get("height").strip()
            weight = request.POST.get("weight").strip()
            collections.insert_one({
                "name":name,
                "height":height,
                "weight":weight
            })
            message = "Insert Success"
        else:
            message = "Type Error"
            
    else:
        message = "Insert Data"
        records = collections.find()
        data = list()
        for rec in records:
            t = dict()
            t['name'] = rec['name']
            t['height'] = rec['height']
            t['weight'] = rec['weight']
            t['bmi'] = round(float(t['weight']) / (int(t['height']) / 100) ** 2, 2)
            data.append(t)
    return render(request, "ch08_bmi.html", locals())

def ch09_test_cookie(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        message = "cookie supported!"
    else:
        message = "cookie not supported"
    request.session.set_test_cookie()

    return render(request, 'ch08_post.html', locals())

def ch09_post(request):
    quote = random.choice(quotes)
    
    if request.user.is_authenticated:
        username = request.user.username
        useremail = request.user.email
        try:
            user = User.objects.get(username=username)
            diaries = ch09_Diary.objects.filter(user=user).order_by('-ddate')
        except Exception as e:
            print(e)
            pass
    messages.get_messages(request)
    # if 'username' in request.session and request.session['username'] != None:
    #     username = request.session['username']
    #     useremail = request.session['useremail']
    #     message = messages.get_messages(request)
    return render(request, 'ch09_post.html', locals())

def ch09_login(request):
    quote = random.choice(quotes)
    if request.method == "POST":
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            user = authenticate(username = login_name, password = login_password)
            if user != None:
                if user.is_active:
                    auth.login(request, user)
                    messages.add_message(request, messages.SUCCESS, "成功登入")
                    return redirect('/ch09_post/')
                else:
                    messages.add_message(request, messages.WARNING, "帳號尚未啟用")

            else:
                messages.add_message(request, messages.WARNING, "登入失敗")
        else:
            messages.add_message(request, messages.INFO, "請檢查輸入的欄位內容")
    else:
        login_form = forms.LoginForm()
    return render(request, 'ch09_login.html', locals())

def ch09_logout(request):
    quote = random.choice(quotes)
    auth.logout(request)
    messages.add_message(request, messages.INFO, "成功登出")
    return redirect('/ch09_post/')
    # if 'username' in request.session:
    #     Session.objects.all().delete()
    #     return redirect('/ch09_login/')
    # return redirect('/ch09_post/')

@login_required(login_url='/ch09_login/')
def ch09_userinfo(request):
    quote = random.choice(quotes)

    if request.user.is_authenticated:
        username = request.user.username
    try:
        user = User.objects.get(username=username)
        userinfo = ch09_Profile.objects.get(user=user)
    except:
        print("User Info ERROR")
    return render(request, 'ch09_userinfo.html', locals())

    # if 'username' in request.session:
    #     username = request.session['username']
    # else:
    #     return redirect('/ch09_login/')
    # try:
    #     userinfo = models.ch09_User.objects.get(name=username)
    # except:
    #     pass
    # return render(request, 'ch09_userinfo.html', locals())

@login_required(login_url='/ch09_login/')
def ch09_postDiary(request):
    quote = random.choice(quotes)
    if request.user.is_authenticated:
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request=request)

    if request.method == "POST":
        user = User.objects.get(username=username)
        diary = ch09_Diary(user=user)
        post_form = forms.DiaryForm(request.POST, instance=diary)
        if post_form.is_valid():
            messages.add_message(request, messages.INFO, "日記已儲存")
            post_form.save()
            return HttpResponseRedirect('/ch09_post/')
        else:
            messages.add_message(request, messages.INFO, "要張貼日誌，每一個欄位都要填...")
    else:
        post_form = forms.DiaryForm()
        messages.add_message(request, messages.INFO, "要張貼日誌，每一個欄位都要填...")
    return render(request, 'ch09_postDiary.html', locals())

def ch09_csvdata(request):
    quote = random.choice(quotes)
    data = csv_data.objects.all()
    return render(request, 'ch09_csvdata.html', locals())

def ch09_plotly(request):
    quote = random.choice(quotes)
    data = csv_data.objects.all()
    labels = [d.name for d in data]
    values = [d.num for d in data]
    plot_div = plot([go.Bar(y=labels, x=values, 
                            orientation='h')], output_type='div')

    # x = np.linspace(0, 2*np.pi, 360)
    # y1 = np.sin(x)
    # y2 = np.cos(x)
    # plot_div = plot([go.Scatter(x=x, y=y1, mode='lines', name='SIN', text='Title', opacity=0.8,
    #                             marker_color='green'), go.Scatter(x=x, y=y2, mode='lines', name='COS', opacity=0.8,
    #                                                               marker_color='green')], output_type='div')

    return render(request, 'ch09_plotly.html', locals())

def ch09_plotly_3D(request):
    quote = random.choice(quotes)
    filename = os.path.join(settings.BASE_DIR, "csv/3d.csv")
    with open(filename, "r", encoding="utf-8") as fp:
        rawdata = fp.readlines()
    rawdata = [(float(d.split(",")[0]), float(d.split(",")[1]), float(d.split(",")[2]), float(d.split(",")[3])) for d in rawdata]
    chart_data = np.array(rawdata).T
    plot_div = plot([go.Scatter3d(x=chart_data[0],
                                  y=chart_data[1],
                                  z=chart_data[3],
                                  mode='markers',
                                  marker=dict(size=2, symbol='circle'))], output_type='div')
    
    return render(request, 'ch09_plotly_3D.html', locals())

@login_required(login_url='/ch09_login/')
def ch10_userinfo(request):
    quote = random.choice(quotes)

    if request.user.is_authenticated:
        username = request.user.username
    user = User.objects.get(username=username)
    try:
        profile = ch09_Profile.objects.get(user=user)
    except:
        profile = ch09_Profile(user=user)

    if request.method == "POST":
        profile_form = forms.ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            messages.add_message(request, messages.INFO, "個人資料已儲存")
            profile_form.save()
            return redirect('/ch10_userinfo/')
        else:
            messages.add_message(request, messages.INFO, "要修改資料，每一個欄位都要填...")
    else:
        profile_form = forms.ProfileForm()

    return render(request, 'ch10_userinfo.html', locals())
