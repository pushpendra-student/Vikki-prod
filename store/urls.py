from pprint import pprint
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter, SimpleRouter

router = SimpleRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)
pprint(router.urls)

urlpatterns = [


]
