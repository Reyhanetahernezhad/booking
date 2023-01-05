import django_filters
from django_filters import rest_framework as filters
from residences.models import *
from transportations.models import *
from reservation.models import *


class AirplaneFilter(filters.FilterSet):
    class Meta:
        fields = {

            'flight_type': 'exact',
            'origin': 'exact',
            'destination': 'exact',
            'departure_date': 'exact',
            'arrival_date': 'exact',
            'flight_class': 'exact',

        }


class HotelRoomFilter(filters.FilterSet):
    class Meta:
        fields = {

            'name': 'exact',
            'location': 'exact',
            'rate': ['exact', 'gte'],
            'passenger_num': ['exact', 'gte', 'lte'],
            'checkin': ['gte', 'lte'],
            'checkout': ['gte', 'lte']

        }
