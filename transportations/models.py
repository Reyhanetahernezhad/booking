from django.core.validators import MinValueValidator
from django.db import models


class AbstractTransportation(models.Model):

    flighttype_choices = (
        ('international', 'international'),
        ('local', 'local')
    )

    flight_type = models.CharField(choices=flighttype_choices, max_length=30)
    origin = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    price = models.BigIntegerField()
    company = models.CharField(max_length=30)
    departure_time = models.DateTimeField(auto_now_add=False)
    arrival_time = models.DateTimeField(auto_now_add=False)
    departure_date = models.DateTimeField(auto_now_add=False)
    arrival_date = models.DateTimeField(auto_now_add=False)
    capacity = models.IntegerField()

    class Meta:
        abstract = True


class Airplane(AbstractTransportation):

    class_choices = (
        ("Economy Class", "Economy Class"),
        ("Premium Economy Class", "Premium Economy Class"),
        ("Business Class", "Business Class"),
        ("First-Class", "First-Class")
    )
    flight_class = models.CharField(choices=class_choices, max_length=30)
    passenger = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
