# import os
# import importlib.resources
from PIL import Image, ImageDraw, ImageFont

# 設定資料
msg = u"就是這樣!!"
font_size = 48
fill = (0,0,0,255)  # 顏色

# 開啟要貼文字上去的圖片
# image_file = Image.open(os.path.abspath("static/images/5.jpg"))
image_file = Image.open("static/images/6.jpg")
# im_w, im_h = image_file.size

# 建立Image物件
im0 = Image.new('RGBA', (1,1))
dw0 = ImageDraw.Draw(im0)

# 建立FreeTypeFont物件
# with importlib.resources.path("demo_font", "kaiu.ttf") as path:
#     with open(path, "rb") as f:
#         font = ImageFont.truetype(f, font_size)
font = ImageFont.truetype("./test_ttf/demo_font/kaiu.ttf", font_size)

# 取得文字的大小
# textsize()已經淘汰，用textbbox()或textlength()取代
fn_left, fn_top, fn_right, fn_bottom = dw0.textbbox((0,0), text=msg, font=font)
# fn = dw0.textlength(text=msg, font=font)
# im = Image.new('RGBA', (int(fn), int(fn)), (255,0,0,0))

# 建立只有文字的Image物件
im = Image.new('RGBA', (fn_right, fn_bottom), (255,0,0,0))
dw = ImageDraw.Draw(im)
dw.text((0,0), msg, font=font, fill=fill)
# 把文字貼到圖片上
image_file.paste(im, (30,50), im)
# 儲存圖片
image_file.save('output4.jpg')