
release: python manage.py migrate
<<<<<<< HEAD
web: gunicorn storefront.wsgi
=======
web: gunicorn vikki_prod.wsgi --log-file -
>>>>>>> e49a0ffa3d04198ca8b9f640d2243412e1da0909
worker: celery -A storefront worker