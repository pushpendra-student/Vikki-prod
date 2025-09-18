

from .common import *

SECRET_KEY = 'django-insecure-mxni!0kpqzszdch7_i4dcy2dn^8icyyb5e6a1e!wv+=ybq=8m$'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': 'Pushpendra@123'
    }
}


CELERY_BROKER_URL = 'redis://localhost:6379/1'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
