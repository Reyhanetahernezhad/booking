from residences.api.serializer import HotelRoomSerializer
from rest_framework import viewsets, mixins
from residences.models import HotelRoom
from django_filters import rest_framework as filters
from filter.filtering import HotelRoomFilter


class HotelRoomViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):

    queryset = HotelRoom.objects.all()
    serializer_class = HotelRoomSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HotelRoomFilter

