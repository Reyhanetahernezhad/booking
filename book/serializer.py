from rest_framework import serializers
from book.models import *


class BookSerializer(serializers.ModelSerializer):
    class meta:
        model = AirplaneReservation
        fields = ('id','reservation_choices', 'user', 'reservation_time', 'created_time', 'modified_time', 'airplane',
                  'is_valid')
