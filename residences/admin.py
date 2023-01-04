from django.contrib import admin
from residences.models import HotelRoom


class AdminHotelRoom(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'price')


admin.site.register(HotelRoom, AdminHotelRoom)