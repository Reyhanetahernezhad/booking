from django.urls import path
from residences.api import views

urlpatterns = [
    path('hotellist/', views.list.as_view(), name='list_HotelRoom'),
    path('airplanelist/', views.list.as_view(), name='list_Airplane'),

]