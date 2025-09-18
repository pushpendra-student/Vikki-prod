release: python manage.py migrate
web: python manage.py collectstatic --noinput && gunicorn storefront.wsgi:application --bind 0.0.0.0:$PORT
worker: celery -A storefront worker