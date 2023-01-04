from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from reservation.serializer import HotelRoomReservationSerializer
from residences.models import HotelRoom


class HotelRoomAPIView(APIView):
    def post(self, request, pk):
        serializer = HotelRoomReservationSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)
