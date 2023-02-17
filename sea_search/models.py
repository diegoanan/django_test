from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateField()
    region = models.CharField(max_length=100)
    tipo_proyecto = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

