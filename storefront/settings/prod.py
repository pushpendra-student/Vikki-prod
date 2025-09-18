import os
from .common import *
import dj_database_url

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['vikki-prod-production.up.railway.app']

DATABASE_URL = f"mysql://{os.environ.get('MYSQLUSER')}:{os.environ.get('MYSQLPASSWORD')}@{os.environ.get('MYSQLHOST')}:{os.environ.get('MYSQLPORT', '3306')}/{os.environ.get('MYSQLDATABASE')}"
DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=600, conn_health_checks=True)
}

CSRF_TRUSTED_ORIGINS = ['https://vikki-prod-production.up.railway.app']
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
