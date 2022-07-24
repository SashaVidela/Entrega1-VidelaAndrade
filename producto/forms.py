
from django import forms

class BusquedaMonitor(forms.Form):
    marca = forms.CharField(max_length=20, required=False)