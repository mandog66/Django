import random
import os
import glob
from PIL import Image, ImageDraw, ImageFont
from uuid_upload_path import uuid

from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from mysite import forms


def mergepic(filename, msg, font_size, x, y):
    fill = (0, 0, 0, 255)
    image_file = Image.open(os.path.join(
        settings.BASE_DIR, 'static', 'images', filename))
    im0 = Image.new('RGBA', (1, 1))
    dw0 = ImageDraw.Draw(im0)
    # font = ImageFont.truetype("test_ttf/demo_font/kaiu.ttf", font_size)
    font = ImageFont.truetype(os.path.join(
        settings.BASE_DIR, 'test_ttf', 'demo_font', 'kaiu.ttf'), font_size)
    fn_left, fn_top, fn_right, fn_bottom = dw0.textbbox(
        (0, 0), text=msg, font=font)
    im = Image.new('RGBA', (fn_right, fn_bottom), (255, 0, 0, 0))
    dw = ImageDraw.Draw(im)
    dw.text((0, 0), msg, font=font, fill=fill)
    image_file.paste(im, (x, y), im)
    saved_filename = uuid() + '.jpg'
    image_file.save(os.path.join(settings.BASE_DIR, "media", saved_filename))
    return saved_filename


def index(request):
    messages.get_messages(request)
    pics = random.sample(range(1, 11), 6)
    return render(request, 'index.html', locals())

# def gen(request):
#     messages.get_messages(request)
#     backfile = glob.glob('{}/static/images/*.jpg'.format(settings.BASE_DIR))
#     if request.method == 'POST':
#         form = forms.GenForm(request.POST)
#         if form.is_valid():
#             saved_filename = mergepic(request.POST.get('backfile'),
#                                       request.POST.get('msg'),
#                                       int(request.POST.get('font_size')),
#                                       int(request.POST.get('x')),
#                                       int(request.POST.get('y')),)
#     else:
#         form = forms.GenForm(backfile)
#     return render(request, 'gen.html', locals())


def gen(request):
    messages.get_messages(request)
    backfile = glob.glob('{}/static/images/*.jpg'.format(settings.BASE_DIR))
    # 讓下列選單是排序狀態
    url = '/usr/src/app/ch15/static/images/'
    num_list = [eval(os.path.basename(bf).split('.', 1)[0]) for bf in backfile]
    num_list.sort()
    backfile = [url + str(num) + '.jpg' for num in num_list]

    if request.method == 'POST':
        form = forms.GenForm(request.POST)
        if form.is_valid():
            saved_filename = mergepic(request.POST.get('backfile'),
                                      request.POST.get('msg'),
                                      int(request.POST.get('font_size')),
                                      int(request.POST.get('x')),
                                      int(request.POST.get('y')),)
        else:
            print("Not valid!!")
        # saved_filename = mergepic(request.POST.get('backfile'),
        #                             request.POST.get('msg'),
        #                             int(request.POST.get('font_size')),
        #                             int(request.POST.get('x')),
        #                             int(request.POST.get('y')),)
    else:
        form = forms.GenForm(backfile)
    return render(request, 'gen.html', locals())


def save_bcakfile(f):
    '''
    將上傳的背景圖片名稱做唯一性
    並將檔案寫入
    '''
    target = os.path.join(settings.BASE_DIR, 'media', uuid() + '.jpg')
    with open(target, 'wb') as des:
        for chunk in f.chunks():
            des.write(chunk)
    return os.path.basename(target)


@login_required
def vip(request):
    messages.get_messages(request)
    custom_backfile = None

    # 判斷背景圖片有沒有上傳新圖片
    # request.session.items()
    # output : dict_items([('_auth_user_id', '1'), ('_auth_user_backend', 'django.contrib.auth.backends.ModelBackend'),
    #                       ('_auth_user_hash', '425bde1ce51a32644e386a42d1029cfbca3e34c3898c20f6c40e479e10bb01ba'),
    #                       ('custom_backfile', 'LQhqgodtQlCx6TJVtzvAfA.jpg')])
    if 'custom_backfile' in request.session:

        # 判斷背景圖片檔案名稱長度
        # 進去網站就會看到的背景圖片(預設1.jpg)
        if len(request.session.get('custom_backfile')) > 0:
            custom_backfile = request.session.get('custom_backfile')
        else:
            print("####################################################")
            print("request.session.get('custom_backfile') < 0")
            print("####################################################")
    else:
        print("####################################################")
        print("custom_backfile not in session!")
        print("####################################################")

    if request.method == 'POST':
        # 判斷是否為上傳背景圖片的表單
        # 是上傳背景圖片的表單
        # request.POST
        # output : <QueryDict: {'csrfmiddlewaretoken': ['Ac5i2Jay54riV1CUANeUeXpRMgnEsLQurI4yiOVZGOtcX7HvPEIGk5SrSK668Heg'],
        #                        'change_backfile': ['變更圖片']}>
        if 'change_backfile' in request.POST:

            # request.FILES
            # output : <MultiValueDict: {'file': [<InMemoryUploadedFile: 3ewsKWapRC6NCmaBs2nwlQ.jpg (image/jpeg)>]}>
            # request.FILES['file']
            # output : 3ewsKWapRC6NCmaBs2nwlQ.jpg
            upload_form = forms.UploadForm(request.POST, request.FILES)
            if upload_form.is_valid():
                custom_backfile = save_bcakfile(request.FILES['file'])
                request.session['custom_backfile'] = custom_backfile
                messages.add_message(
                    request, messages.WARNING, "Upload Success!!")
                return redirect("/vip/")
            else:
                messages.add_message(
                    request, messages.WARNING, "Upload Faile!!")
                return redirect("/vip/")
        # 不是上傳背景圖片的表單
        # 只是要設定貼文字在背景圖片上的表單
        else:
            form = forms.CustomForm(request.POST)
            # 判斷要製作的背景圖片有沒有更改過
            # 沒有被更改(一開始進去看到的背景圖片)
            if custom_backfile is None:
                back_file = os.path.join(
                    settings.BASE_DIR, "/static/images/1.jpg")
            # 有被更改過(上傳的圖片當作要製作的背景圖片)
            else:
                back_file = os.path.join(
                    settings.BASE_DIR, 'media', custom_backfile)
            # 製作圖片
            saved_filename = mergepic(back_file,
                                      request.POST.get('msg'),
                                      int(request.POST.get('font_size')),
                                      int(request.POST.get('x')),
                                      int(request.POST.get('y')),)
    else:
        form = forms.CustomForm()
        upload_form = forms.UploadForm()
        print("####################################################")
        print("request.method == GET")
        print("####################################################")

    return render(request, 'vip.html', locals())
