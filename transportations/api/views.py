from residences.api.serializer import HotelRoomSerializer
from rest_framework import viewsets, mixins
from residences.models import HotelRoom
from django_filters import rest_framework as filters
from filter.filtering import AirplaneFilter
from transportations.api.serializer import AirplaneSerializer
from transportations.models import Airplane


class AirplaneViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AirplaneFilter
