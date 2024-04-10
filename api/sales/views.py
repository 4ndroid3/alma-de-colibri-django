from rest_framework import mixins, viewsets

from api.sales.serializers import CartSerializer, SaleSerializer
from sales.models import Cart, Sale


class SaleView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class CartView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
