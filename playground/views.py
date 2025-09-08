from django.shortcuts import render
from .tasks import notify_customers

# celery - A storefront worker - -pool = solo - -loglevel = info


def say_hello(request):
    notify_customers.delay('hello')
    return render(request, 'hello.html')
