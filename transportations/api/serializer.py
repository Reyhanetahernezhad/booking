from rest_framework import serializers
from transportations.models import *


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ('origin', 'destination', 'company', 'departure_time', 'arrival_time',
                  'flight_class', 'passenger', )
