# C:\repos\Hoteles\Reservaciones\models.py
from django.db import models

class Reservacion(models.Model):
    tipo = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    numero_tarjeta = models.CharField(max_length=16)
    fecha = models.DateField()

    class Meta:
        db_table = 'reservaciones'  # Especifica el nombre de la tabla
