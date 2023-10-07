import os
backfile = ['/usr/src/app/ch15/static/images/1.jpg',
            '/usr/src/app/ch15/static/images/10.jpg',
            '/usr/src/app/ch15/static/images/2.jpg',
            '/usr/src/app/ch15/static/images/3.jpg',
            '/usr/src/app/ch15/static/images/4.jpg',
            '/usr/src/app/ch15/static/images/5.jpg',
            '/usr/src/app/ch15/static/images/6.jpg',
            '/usr/src/app/ch15/static/images/7.jpg',
            '/usr/src/app/ch15/static/images/8.jpg',
            '/usr/src/app/ch15/static/images/9.jpg']

# choices=[(os.path.basename(bf), os.path.basename(bf)) for bf in backfiles]

# tmp = [(num, os.path.basename(bf)) for num, bf in enumerate(backfile, 1)]
# print(tmp)
# def sort_bf(url):
#     url.sort()
#     return url
#     [str(os.path.basename(bf).split('.', 1)[0]) for bf in backfile]
#     a = [url + num for num in ([str(os.path.basename(bf).split('.', 1)[0]) for bf in backfile])]
#     print(a)
#     for bf in backfile:
#         sort_bf_list.append(str(os.path.basename(bf).split('.', 1)[0]))
#     sort_bf_list.sort()
#     return sort_bf_list
url = '/usr/src/app/ch15/static/images/'
num_list = [eval(os.path.basename(bf).split('.', 1)[0]) for bf in backfile]
num_list.sort()
sort_list = [url + str(num) + '.jpg' for num in num_list]
