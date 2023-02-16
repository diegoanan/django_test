from django.contrib import admin
from .models import BikeStation
# Generar vista en el administrador para visualizar la información obtenida
class BikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'free_bikes', 'empty_slots')

# Registrar el modelo y la vista en el administrador
admin.site.register(BikeStation, BikeAdmin)
