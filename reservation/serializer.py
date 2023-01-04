from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from reservation.models import *
from residences.models import *
from transportations.models import *


class AirplaneReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirplaneReservation
        fields = ('id', 'reservation_choices', 'user', 'reservation_time', 'airplane', 'is_valid')

    def create(self, validated_data):
        airplane = Airplane.objects.get(id=self.get_value('flight'))

        if Airplane.passenger < Airplane.capacity:
            Airplane.capacity = Airplane.capacity-1
            Airplane.save()
            super(AirplaneReservationSerializer, self).create(validated_data)
        else:
            raise ObjectDoesNotExist('No more available sit')


class HotelRoomReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomReservation
        fields = ('id', 'name', 'Room', 'passenger_num', 'is_booked', 'checkin', 'checkout', 'facility')

    def create(self, validated_data):
        checkin = self.get_value('checkin')
        checkout = self.get_value('checkout')

        status_1 = HotelRoomReservation.objects.filter(Room_id=self.get_value('Room'),
                                                       checkin__lte=checkin, checkout__gte=checkout).exists()

        status_2 = HotelRoomReservation.objects.filter(Room_id=self.get_value('Room'),
                                                       checkin__gte=checkin, checkout__gte=checkout).exists()

        status_3 = HotelRoomReservation.objects.filter(Room_id=self.get_value('Room'),
                                                       checkin__gte=checkin, checkout__lte=checkout).exists()

        status_4 = HotelRoomReservation.objects.filter(Room_id=self.get_value('Room'),
                                                       checkin__lte=checkin, checkout__lte=checkout).exists()

        if status_1 or status_2 or status_3 or status_4:
            raise ObjectDoesNotExist('no more available room')
        else:
            super(HotelRoomReservationSerializer, self).create(validated_data)



