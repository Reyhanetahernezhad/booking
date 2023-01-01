from rest_framework import serializers
from transportations.models import *


class AirplaneSerializer(serializers.ModelSerializer):
    class meta:
        model = Airplane
        fields = ('origin', 'destination', 'price', 'company', 'departure_time', 'arrival_time',
                  'flight_class', 'passenger', )
