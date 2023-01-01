from django.contrib import admin
from .models import *

class AdminAirplane(admin.ModelAdmin):
    list_display = ('id', 'origin', 'destination')


admin.site.register(Airplane, AdminAirplane)