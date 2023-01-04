from django.urls import path
from .serializer import *
from .views import HotelRoomAPIView


urlpatterns = [
    path('hotelreservation/', HotelRoomAPIView.as_view(), name='HotelRoom_reservation'),
    path('airplaneraservation/', HotelRoomAPIView.as_view(), name='Airplane_reservation'),

]