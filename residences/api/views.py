from django.shortcuts import render
from rest_framework import generics
from residences.api.serializer import HotelRoomSerializer
from residences.models import HotelRoom


class HotelRoomList(generics.ListAPIView):
    queryset = HotelRoom.objects.all()
    serializer_class = HotelRoomSerializer

