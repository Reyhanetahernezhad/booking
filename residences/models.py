from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class AbstractResidence(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    rate = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    avatar = models.ImageField(upload_to='residence/images/', null=True, blank=True)
    price = models.BigIntegerField()

    class Meta:
        abstract = True


class Room(AbstractResidence):

    facility_choices = (
       ('1', 'parking'),
       ('2', 'breakfast'),
       ('3', 'fitness center'),
       ('4', 'free wifi'),

    )

    star_choices = (
        ('one_star', '1_star'),
        ('two_star', '2_star'),
        ('three_star', '3_star'),
        ('four_star', '4_star'),
        ('five_star', '5_star'),
    )

    room_num = models.SmallIntegerField()
    passenger_num = models.SmallIntegerField()
    avatar = models.ImageField(upload_to='room/images/', null=True, blank=True)
    is_booked = models.BooleanField(default=False)
    checkin = models.BooleanField(default=False)
    checkout = models.BooleanField(default=False)
    facility = models.CharField(choices=facility_choices, max_length=30)
    rate = models.CharField(choices=star_choices, max_length=30)
