from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Monitores


class ListaMonitores(ListView):
    model=Monitores
    template_name = 'monitores/lista_monitores.html'
    
    
class CrearMonitor(CreateView):
    model=Monitores
    template_name = 'monitores/crear_monitor.html'
    success_url = '/producto/monitores'
    fields = ['marca', 'modelo', 'precio']
    
    
class EditarMonitor(LoginRequiredMixin, UpdateView):
    model=Monitores
    template_name = 'monitores/editar_monitor.html'
    success_url = '/producto/monitores'
    fields = ['marca', 'modelo', 'precio']
    


class EliminarMonitor(LoginRequiredMixin, DeleteView):
    model=Monitores
    template_name = 'monitores/eliminar_monitor.html'
    success_url = '/producto/monitores'


class MostrarMonitor(DetailView):
    model = Monitores
    template_name = 'monitores/mostrar_monitor.html'    
