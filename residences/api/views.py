from django.shortcuts import render
from rest_framework import generics
from residences.api.serializer import RoomSerializer
from residences.models import Room


class RoomList(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

