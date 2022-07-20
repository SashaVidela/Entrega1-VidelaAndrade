
from django import forms

class BusquedaCelular(forms.Form):
    marca = forms.CharField(max_length=20, required=False)