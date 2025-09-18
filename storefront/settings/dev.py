

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

REDIS_URL = os.environ.get('REDIS_URL')

CELERY_BROKER_URL = REDIS_URL

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
