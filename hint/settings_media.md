# Setting the media config in Django

## Follow these steps

* step 1 :

  * settings.py

    ```python
    MEDIA_ROOT = BASE_DIR / 'media'
    MEDIA_URL = 'media/'
    ```

* step 2 :

  * urls.py

    ```python
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

* step 3 :

  * Create `media` folder

    ```bash
    mkdir ${PROJECTNAME}/media
    ```
