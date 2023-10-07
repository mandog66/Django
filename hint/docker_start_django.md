# 完成在Docker部屬Django

* ## 建立一個資料夾`${folder_name}`後創建/複製[需要的檔案](<doc/basic docker files>)到`${folder_name}`，並進到資料夾內

  * 選擇需要的檔案就好

```tree
${folder_name}
    .env
    docker-compose-db.yml
    docker-compose-mongodb.yml
    docker-compose.yml
    Dockerfile
    requirements.txt
```

* ## 配置每個檔案，像是檔案名稱、路徑、變數

```bash
code .\requirements.txt & check the model

code Dockerfile & check the command

code .env & check the variables

code docker-compose.yml & check the services

code ...
```

* ## 建立django框架

  * 注意資料夾位置，要用 **`反斜線`**

    ```docker
    docker compose run --rm web django-admin startproject ${COMPOSE_PROJECT_NAME}
    ```

  * 想要在Project裡面建立App，可以使用指令設定App路徑，不過要先創建`${APP_NAME}`資料夾

    * `django-admin startapp` 和 `python manage.py startapp` 執行上沒有差異，不過在測試上 django-admin startapp 才能在docker執行

    ```bash
    mkdir ${COMPOSE_PROJECT_NAME}/${APP_NAME}
    ```

    ```docker
    docker compose run --rm web django-admin startapp ${APP_NAME} ./${COMPOSE_PROJECT_NAME}/${APP_NAME}
    ```

    > ## 如果出現錯誤
    >
    > ### 1. TypeError: argument of type 'PosixPath' is not iterable
    >
    > * 去settings.py裡面的`DATABASES`做更改，我猜是django版本問題
    >
    >      ```python
    >      DATABASES = {
    >          'default': {
    >              'ENGINE': 'django.db.backends.sqlite3',
    >              'NAME': str(BASE_DIR / 'db.sqlite3'),
    >          }
    >      }
    >      ```
    >
    > ### 2. TypeError: unsupported operand type(s) for /: 'str' and 'str'
    >
    > * 去settings.py裡面的`STATIC`做更改，我猜是django版本問題
    >
    >    ```python
    >    STATIC_URL = '/static/'
    >    STATIC_ROOT = BASE_DIR + '/staticfiles'
    >    STATICFILES_DIRS = [
    >        BASE_DIR + '/static'
    >    ]
    >    ```
    >
    > ### 3. CommandError: '.\ch10_test\mysite\' is not a valid app directory. Please make sure the directory is a valid identifier
    >
    > * 路徑`不要`用反斜線
    >
    >>

* ## 下面是我認為基礎的設置，其他的功能可以看[Github](https://github.com/mandog66/django4)的code

  * settings.py

    ```python
    DEBUG = True

    ALLOWED_HOSTS = ['*']

    # Application definition
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        '${APP_NAME}',
    ]

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/4.1/topics/i18n/
    LANGUAGE_CODE = 'zh-hant'
    TIME_ZONE = 'Asia/Taipei'
    USE_I18N = True
    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.1/howto/static-files/
    STATIC_URL = 'static/'
    STATIC_ROOT = BASE_DIR / 'staticfiles/'
    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]

    # 要記得在專案資料夾內創建media資料夾
    MEDIA_ROOT = BASE_DIR / 'media'
    MEDIA_URL = 'media/'
    ```

  * urls.py

    ```python
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

  * 放置模板的位置

    * 這裡分成兩個temaplates資料夾，一個在APP內，另一個在專案內，想法是想分開這是APP相關的html還是基礎網頁的html，像是`base.html`、`header.html`、`footer.html`、`index.html`。要這樣分開成兩個資料夾需要先在settings.py中TEMPLATES的`APP_DIRS`設成`True`，這樣當需要templates時會先從APP_DIRS開始找，如果沒有找到才會到`DIRS`設定的路徑尋找檔案。當然，也可以只有專案內的資料夾，就是html全部放在一起。

    ```bash
    mkdir ${COMPOSE_PROJECT_NAME}/templates & mkdir ${COMPOSE_PROJECT_NAME}/templates

    mkdir ${COMPOSE_PROJECT_NAME}/templates & mkdir ${COMPOSE_PROJECT_NAME}/${APP_NAME}/templates
    ```

  * 放置模板標籤的位置
    * [標籤](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/)可以設定新的方法。

    * 創建必要的檔案，如下 :

      * \_\_init__.py
      * 模板標籤名稱.py

    ```bash
    mkdir ${COMPOSE_PROJECT_NAME}/${APP_NAME}/templatetags
    ```

  * 放置靜態資料的位置
    * 這個單純就是收集放在各個路徑的[靜態資料](https://docs.djangoproject.com/en/4.2/ref/contrib/staticfiles/)，將他們收集到同一個資料夾內，方便專案使用。
    * 設定必要配置 :
      * 要將靜態資料收集在哪的變數

        ```python
          STATIC_ROOT = 'staticfiles/'
        ```

      * 要尋找靜態資料的路徑

        ```python
          STATICFILE_DIR = [
              BASE_DIR + '/static'
          ]
        ```

      * 執行指令

        ```DOCKER
            docker compose run --rm web python ${COMPOSE_PROJECT_NAME}/manage.py collectstatic
        ````

> [!NOTE]
>
> ## 如果在啟動容器前，發現需要 pip install Package，要直接在容器內下載，docker compose run --rm 會因為刪除容器而失去下載好的package
>
> ```docker
> docker compose up -d
> ```
>
> ```bash
> python manage.py makemigrations
> ```
>
> ```BASH
> python manage.py migrate
> ```
