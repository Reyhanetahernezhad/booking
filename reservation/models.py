from django.db import models
from transportations.models import Airplane
from residences.models import HotelRoom
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL


class AbstractTransportationsReservation(models.Model):
    Reservation_choices = (
        ('canceled', 'canceled'),
        ('reserved', 'reserved')
    )

    reservation_choices = models.CharField(choices=Reservation_choices, max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField()
    total_price = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AirplaneReservation(AbstractTransportationsReservation):
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    is_valid = models.BooleanField(default=True)


class AbstractResidenceReservation(models.Model):
    Reservation_choices = (
        ('canceled', 'canceled'),
        ('reserved', 'reserved')
    )

    reservation_choices = models.CharField(choices=Reservation_choices, max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    total_price = models.IntegerField()


class HotelRoomReservation(AbstractResidenceReservation):
    Room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE)
    is_valid = models.BooleanField(default=True)
