from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from reservation.serializer import HotelRoomReservationSerializer, AirplaneReservationSerializer
from residences.api.serializer import HotelRoomSerializer
from transportations.api.serializer import AirplaneSerializer
from transportations.models import Airplane
from residences.models import HotelRoom


class HotelRoomAPIView(APIView):
    def get(self, request, pk):
        hotel = HotelRoom.objects.get(id=pk)
        serializer = HotelRoomSerializer(hotel)
        return JsonResponse(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = HotelRoomReservationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class AirplaneAPIView(APIView):
    def get(self, request, pk):
        airplane = Airplane.objects.get(id=pk)
        serializer = AirplaneSerializer(airplane)
        return JsonResponse(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = AirplaneReservationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)
