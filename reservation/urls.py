from django.urls import path
from .serializer import *
from .views import HotelRoomAPIView, AirplaneAPIView



urlpatterns = [
    path('hotelreservation/<int:pk>/', HotelRoomAPIView.as_view(), name='HotelRoom_reservation'),
    path('airplaneraservation/<int:pk>/', AirplaneAPIView.as_view(), name='Airplane_reservation'),

]