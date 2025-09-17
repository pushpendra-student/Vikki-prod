
release: python manage.py migrate
web: gunicorn vikki_prod.wsgi --log-file -
worker: celery -A storefront worker