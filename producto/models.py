from django.db import models

class Monitores(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=50)
    precio = models.FloatField()
    
    def __str__(self):
        return f'Se encontró información del monitor {self.marca} {self.modelo}'