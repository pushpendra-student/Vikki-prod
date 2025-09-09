
from decimal import Decimal
import pytest
from rest_framework import status
from store.models import Collection, Product
from model_bakery import baker


@pytest.fixture
def create_product(api_client):
    def do_create_product(product):
        return api_client.post('/store/products/', product)
    return do_create_product


@pytest.mark.django_db
class TestcreateProduct:
    def test_if_user_is_anonymous_returns_401(self, create_product):
        response = create_product({'title': 'p'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, authenticated, create_product):
        authenticated()

        response = create_product({'title': 'p'})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(self, authenticated, create_product):
        authenticated(is_staff=True)

        response = create_product({'title': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_returns_201(self, authenticated, create_product):
        authenticated(is_staff=True)

        collection = Collection.objects.create(title='a')

        response = create_product({
            "title": "p",
            "slug": "-",
            "inventory": 10,
            "unit_price": 100,
            "collection": collection.id
        })

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0


@pytest.mark.django_db
class TestRetrieveProduct:
    def test_if_product_exists_returns_200(self, authenticated, api_client):
        authenticated(is_staff=True)

        collection = baker.make(Collection)
        product = baker.make(Product, collection=collection)
        response = api_client.get(f'/store/products/{product.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': product.id,
            'title': product.title,
            'unit_price': product.unit_price,
            'collection': collection.id,
            'inventory': product.inventory,
            'description': None,
            'images': [],
            'price_with_tax': product.unit_price * Decimal(1.1),
            'slug': '-'

        }
