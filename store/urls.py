from pprint import pprint
from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customer', views.CustomerViewSet)
router.register('orders', views.OrderViewSet)

product_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
product_router.register('reviews', views.ReviewViewSet,
                        basename='product-reviews')

# First - parent router , parent prefix name, lookup which api look
cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
# custom api prefix name - items , views , than basename= lookup-custom prefix
cart_router.register('items', views.CartItemViewSet, basename='cart-items')

urlpatterns = router.urls + product_router.urls + cart_router.urls
