from rest_framework import serializers
from residences.models import *

class HotelSerializer(serializers.ModelSerializer):
    class meta:
        model = Hotel
        fields = ('origin', 'destination', 'price', 'company', 'departure_time', 'arrival_time',
                  'flight_class', 'passenger', )