from django.contrib import admin
from .models import Proyecto

#Visualizacion de data en Admin
class SeaDataAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'region', 'tipo_proyecto', 'estado')

admin.site.register(Proyecto, SeaDataAdmin)
