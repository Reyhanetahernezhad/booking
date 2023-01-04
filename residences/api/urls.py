from django.urls import path
from residences.api import views

urlpatterns = [
    path('lists/', views.HotelRoomList.as_view(), name='list_HotelRoom')
]