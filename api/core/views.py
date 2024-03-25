from rest_framework import mixins, viewsets

from api.core.serializers import CitySerializer, UserSerializer
from core.models import City, User


class CityView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class UserView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
