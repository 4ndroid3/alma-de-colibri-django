from rest_framework import mixins, viewsets

from api.products.serializers import CategorySerializer, ProductSerializer
from products.models import Category, Product


class ProductView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer


class CategoryView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all().order_by("id")
    serializer_class = CategorySerializer
