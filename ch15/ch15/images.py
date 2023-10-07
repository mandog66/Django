import os
from PIL import Image

src_url = "{}/ch15/static/src".format(os.getcwd())
dst_url = "{}/ch15/static/images".format(os.getcwd())

def img_rename(dst_url: str) -> None:
    file = 1
    for img in os.listdir(path=dst_url):
        file_name = "{}.jpg".format(file)
        src = os.path.join(dst_url, img)
        dst = os.path.join(dst_url, file_name)
        os.rename(src, dst)
        print("{} rename success".format(file_name))
        file += 1
    return None

def img_resize(src_url: str, dst_url: str) -> None:
    file = 1
    for img in os.listdir(path=src_url):
        file_name = os.path.join(dst_url, "{}.jpg".format(file))
        img_object = Image.open(os.path.join(src_url, img))
        size = (300, 300)
        img_object.resize(size, Image.Resampling.LANCZOS).save(file_name, 'jpeg')
        print("{} resize success".format(img))
        file += 1
    return None

def img_data(dst_url: str) -> None:
    for img in os.listdir(path=dst_url):
        img_object = Image.open(os.path.join(dst_url, img))
        print("Image name : {}".format(img))
        print("Image width : {}".format(img_object.width))
        print("Image height : {}".format(img_object.height))
        print()
    return None

img_data(src_url)
img_resize(src_url, dst_url)
img_data(dst_url)
