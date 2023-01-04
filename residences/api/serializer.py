from rest_framework import serializers
from residences.models import *


class HotelRoomSerializer(serializers.ModelSerializer):
    class meta:
        model = HotelRoom
        fields = ('type', 'location', 'name', 'rate', 'avatar', 'price',
                  'room_num', 'passenger_num', 'is_booked', 'checkin', 'checkout', 'facility' )