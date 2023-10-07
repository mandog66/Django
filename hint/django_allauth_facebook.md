# django-allauth and Facebook Authentication

## django-allauth

* ### Description

  * django-allauth是一個厲害的帳號驗證框架，擁有django-registration-redux的所有帳號驗證功能，也支援社群軟體的第三方驗證功能，像是Faceebook、Google。

    * [django-allauth Doc](https://django-allauth.readthedocs.io/en/latest/index.html)
    * [django-allauth GitHub](https://github.com/pennersr/django-allauth)

* ### Install

  * step 1. Install Package

    ```bash
    pip install django-allauth
    ```

  * step 2. Configuration([django-allauth Doc](https://django-allauth.readthedocs.io/en/latest/index.html)有更詳細訊息)

    * settings.py

    ```python
    # Specify the context processors as follows:
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    # Already defined Django-related contexts here

                    # `allauth` needs this from django
                    'django.template.context_processors.request',
                ],
            },
        },
    ]

    AUTHENTICATION_BACKENDS = [
        # Needed to login by username in Django admin, regardless of `allauth`
        'django.contrib.auth.backends.ModelBackend',

        # `allauth` specific authentication methods, such as login by email
        'allauth.account.auth_backends.AuthenticationBackend',
    ]

    INSTALLED_APPS = [
        # The following apps are required:
        'django.contrib.auth',
        'django.contrib.messages',

        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        # ... include the providers you want to enable:
        'allauth.socialaccount.providers.facebook',
    ]

    MIDDLEWARE = (
        "django.middleware.common.CommonMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",

        # Add the account middleware:
        "allauth.account.middleware.AccountMiddleware",
    )

    # Provider specific settings
    SOCIALACCOUNT_PROVIDERS = {
        'facebook': {
            'METHOD': 'oauth2',
            'SCOPE': ['email', 'public_profile'],
            'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
            'INIT_PARAMS': {'cookie': True},
            'FIELDS': [
                'id',
                'first_name',
                'last_name',
                'middle_name',
                'name',
                'email',
                'name_format',
                'picture',
                'short_name'
            ],
            'EXCHANGE_TOKEN': True,
            'VERIFIED_EMAIL': False,
            'VERSION': 'v13.0',
        }
    }
    ```

    * urls.py

    ```python
    urlpatterns = [
        path('accounts/', include('allauth.urls')),
    ]
    ```

  * step 3. Migrate DB

    ```console
    python manage.py migrate
    ```

## Facebook Authentication

* ### Connecting to Facebook

  * [Facebook Developers](https://developers.facebook.com/apps/?show_reminder=true)

  * Follow the [tutorial](https://www.codesnail.com/facebook-authentication-in-django-using-django-allauth/) and [線上購物_Paypal_Google_付款完成.md](%E7%B7%9A%E4%B8%8A%E8%B3%BC%E7%89%A9_Paypal_Google_%E4%BB%98%E6%AC%BE%E5%AE%8C%E6%88%90.md)
