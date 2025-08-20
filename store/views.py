from django.shortcuts import get_object_or_404
from store.models import Product, Collection
from .serializers import ProductSerializer, CollectionSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django.db.models.aggregates import Count


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {'request': self.request}

    def delete(self, request, pk):
        product = get_object_or_404(Product, pl=pk)
        if product.orderitems.count() > 0:
            return Response({'error': 'Product can not be deleted because it is associated with an order item.'})
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(
        product_count=Count('products')).all()
    serializer_class = CollectionSerializer

    def delete(self, request, pk):
        collection = get_object_or_404(Collection, pk=pk)

        if collection.products.count() > 0:
            return Response({'error': 'Collection can not be deleted because it is associated with Product.'})
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
