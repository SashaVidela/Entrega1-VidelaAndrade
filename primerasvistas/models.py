from django.db import models

class Celulares(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=50)
    fecha_registro = models.DateField(null=True)