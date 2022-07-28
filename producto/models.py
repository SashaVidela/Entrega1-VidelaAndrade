from django.db import models
from ckeditor.fields import RichTextField


class Monitores(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=50)
    precio = models.FloatField()
    descripcion = RichTextField(null=True)
    avatars = models.ImageField(upload_to='avatares', null=True, blank=True)
        
    
    def __str__(self):
        return f'Se encontró información del monitor {self.marca} {self.modelo}'