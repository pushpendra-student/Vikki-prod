
release: python manage.py migrate
web: gunicorn storefront.wsgi --bind 0.0.0.0:$PORT
worker: celery -A storefront worker 


