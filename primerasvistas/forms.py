from django import forms

class FormCelulares(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=50)
    fecha_registro = forms.DateField(required=False)
    
class BusquedaCelulares(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)