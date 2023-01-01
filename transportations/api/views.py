from rest_framework import generics
from .serializer import *
from transportations.models import *


class ListAirplane(generics.ListAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
