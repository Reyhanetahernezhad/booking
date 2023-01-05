from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from reservation.models import *
from residences.models import *
from transportations.models import *


class AirplaneReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirplaneReservation
        fields = ('id', 'reservation_time', 'airplane', 'is_valid', 'total_price')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        airplane = Airplane.objects.get(id=validated_data['airplane'].id)

        if airplane.passenger < airplane.capacity:
            airplane.capacity = airplane.capacity-1
            airplane.save()
            return super(AirplaneReservationSerializer, self).create(validated_data)
        else:
            raise ObjectDoesNotExist('No more available sit')


class HotelRoomReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomReservation
        fields = [
            'reservation_time', 'checkin', 'checkout', 'Room', 'is_valid', 'total_price'
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user

        checkin = validated_data['checkin']
        checkout = validated_data['checkout']

        status_1 = HotelRoomReservation.objects.filter(id=validated_data['Room'].id,
                                                       checkin__lte=checkin, checkout__lte=checkout).exists()

        status_2 = HotelRoomReservation.objects.filter(id=validated_data['Room'].id,
                                                       checkin__gte=checkout, checkout__gte=checkout).exists()

        if status_1 or status_2:
            raise ObjectDoesNotExist('no more available room')

        else:
            return super(HotelRoomReservationSerializer, self).create(validated_data)


