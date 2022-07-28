from django import forms
from ckeditor.fields import RichTextFormField


class FormCelulares(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=50)
    descripcion = RichTextFormField(required=False)
    fecha_registro = forms.DateField(required=False)
    avatars = forms.ImageField(required=False)
    
class BusquedaCelulares(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)


