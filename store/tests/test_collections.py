
from rest_framework import status
import pytest
from model_bakery import baker
from store.models import Collection


@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):  # creating a collection object
        # return a response with created object
        return api_client.post('/store/collections/', collection)
    return do_create_collection  # calling inner function

# AAA(Arrang,Act,Assert)


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(self, create_collection):
        response = create_collection({'title': 'a'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, authenticated, create_collection):
        authenticated()  # is_staff=False means not admin

        response = create_collection({'title': 'a'})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(self, authenticated, create_collection):
        authenticated(is_staff=True)

        response = create_collection({'title': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_returns_201(self, authenticated, create_collection):
        authenticated(is_staff=True)

        response = create_collection({'title': 'a'})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0


@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_exists_returns_200(self, api_client, authenticated):
        authenticated(is_staff=True)

        collection = baker.make(Collection)
        response = api_client.get(f'/store/collections/{collection.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': collection.id,
            'title': collection.title,
            'product_count': 0
        }
