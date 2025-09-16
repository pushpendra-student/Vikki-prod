
from django.shortcuts import render
from rest_framework.views import APIView
import requests
import logging

logger = logging.getLogger(__name__)


class HelloView(APIView):
    def get(self, request):
        try:
            logger.info('Calling Httpbin')
            response = requests.get("http://httpbin.org/delay/2")
            logger.info('Receive the Response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render(request, 'hello.html')
