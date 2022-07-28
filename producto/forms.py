from django import forms
from ckeditor.fields import RichTextFormField


class BusquedaMonitor(forms.Form):
    marca = forms.CharField(max_length=20, required=False)
    

class FormMonitores(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=50)
    precio = forms.FloatField(required=False)
    descripcion = RichTextFormField(required=False)
    avatars = forms.ImageField(required=False)