from django.contrib import admin
from residences.models import Room


class AdminRoom(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'price')


admin.site.register(Room, AdminRoom)