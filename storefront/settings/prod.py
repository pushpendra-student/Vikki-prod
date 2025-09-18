import os
from .common import *
import dj_database_url

# -----------------------------
# Basic settings
# -----------------------------
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    raise ValueError("The SECRET_KEY environment variable is not set!")

ALLOWED_HOSTS = ['vikki-prod-production.up.railway.app']
CSRF_TRUSTED_ORIGINS = ['https://vikki-prod-production.up.railway.app']

# -----------------------------
# Database configuration
# -----------------------------
MYSQL_USER = os.environ.get('MYSQLUSER')
MYSQL_PASSWORD = os.environ.get('MYSQLPASSWORD')
MYSQL_HOST = os.environ.get('MYSQLHOST')
MYSQL_PORT = os.environ.get('MYSQLPORT', '3306')
MYSQL_DB = os.environ.get('MYSQLDATABASE')

if not all([MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DB]):
    raise ValueError("One or more MySQL environment variables are missing!")

DATABASE_URL = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
DATABASES = {
    'default': dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=600,
        conn_health_checks=True
    )
}

# -----------------------------
# Redis / Celery configuration
# -----------------------------
REDIS_PASSWORD = os.environ.get('REDISPASSWORD')
REDIS_HOST = os.environ.get('REDISHOST')
REDIS_PORT = os.environ.get('REDISPORT', '6379')

if not all([REDIS_PASSWORD, REDIS_HOST]):
    raise ValueError("One or more Redis environment variables are missing!")

REDIS_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/1"

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

print("DATABASE_URL:", DATABASE_URL)
print("REDIS_URL:", REDIS_URL)
