from django.contrib import admin
from .models import BikeStation

class BikeStationAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'free_bikes', 'empty_slots')

admin.site.register(BikeStation, BikeStationAdmin)