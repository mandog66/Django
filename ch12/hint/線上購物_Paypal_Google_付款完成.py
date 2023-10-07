# 線上購物只成功在Google，Facebook沒有成功

# 遇到的問題 : 
#     1.購買完成沒有觸發完成付款的Signals
#     2.在Docker使用Ngrok無法執行
#     3.Ngrok無法和localhost:8000連接
#     4.使用Ngrok的網址有CSRF問題
#     5.無法登入購物網站

# 解決方法 : 
#     1.因為我們是要讓Localhost公開，幫助我們可以從外面連近來，所以要使用Ngrok來公開Localhost，否則Paypal完成付款的資訊會被擋住。
#     2.已經寫在"docker-compose-ngrok.yml"裡面，要注意是command: http web:8000的web要寫上去，使用Docker DNS辨識我們的應用程式。
#     3.把docker-compose-ngrok.yml寫好後，要增加config檔(ngrok.yml)，要注意"authtoken"去Ngrok官網登入帳好取得。
#     4.在Localhost:8000可以利用"@csrf_exempt"、"{% csrf_token %}來避免CSRF問題，但是在Ngrok要去settings.py和
#         mysite/__init__.py多增加參數
#             4.1.settings.py
#                 4.1.1.CSRF_TRUSTED_ORIGINS = [
#                     'https://c2e8-2401-e180-88a2-a61f-7d7e-f32d-b1ce-4436.ngrok-free.app', <--網址是Ngrok配給我們的
#                     'https://tight-ultimately-baboon.ngrok-free.app',
#                 ]

#                 4.1.2.CORS_ORIGIN_WHITELIST = [
#                     'https://c2e8-2401-e180-88a2-a61f-7d7e-f32d-b1ce-4436.ngrok-free.app',
#                     'https://tight-ultimately-baboon.ngrok-free.app',
#                 ]
#             4.2.mysite/__init__.py
#                 default_app_config = 'mysite.apps.MysiteConfig'
#     5.這個問題只有在Google可以解決，Facebook還找不到問題。我們要去Google Cloud的憑證裡加入Ngrok配的網址
#         5.1.已授權的 JavaScript 來源
#         5.2.已授權的重新導向 URI(這裡網址要改成http，沒有加s)

# 到這裡完成，可以用Ngrok的網址連到Localhost:8000，隨便加入一些東西到購物車(要登入才能加)並使用Paypal付款
# (有分成business、personal，購買使用personal)，完成付款後要的一些時間就可以看到資料庫的付款變成True。
