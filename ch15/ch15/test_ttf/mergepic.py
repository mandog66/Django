import os
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont
from uuid_upload_path import uuid

def mergepic(msg, font_size, x, y):
    fill = (0,0,0,255)
    image_file = Image.open('static/images/1.jpg')
    # im_w, im_h = image_file.size
    im0 = Image.new('RGBA', (1,1))
    dw0 = ImageDraw.Draw(im0)
    font = ImageFont.truetype("./test_ttf/demo_font/kaiu.ttf", font_size)
    fn_left, fn_top, fn_right, fn_bottom = dw0.textbbox((0,0), text=msg, font=font)
    im = Image.new('RGBA', (fn_right, fn_bottom), (255,0,0,0))
    dw = ImageDraw.Draw(im)
    dw.text((0,0), msg, font=font, fill=fill)
    image_file.paste(im, (x, y), im)
    saved_filename = uuid() + '.jpg'
    image_file.save(os.path.join(settings.BASE_DIR, "media", saved_filename))
    return saved_filename