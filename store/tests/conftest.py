from rest_framework.test import APIClient
import pytest
from django.contrib.auth.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticated(api_client):
    # with that we do not have to specify is_staff value
    def do_authenticated(is_staff=False):
        return api_client.force_authenticate(user=User(is_staff=is_staff))
    return do_authenticated
