from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import BusquedaMonitor
from .models import Monitores


class ListaMonitores(ListView):
    model=Monitores
    template_name = 'monitores/lista_monitores.html'

    def get_queryset(self):
        marca = self.request.GET.get('marca', '')
        if marca:
            object_list = self.model.objects.filter(marca__icontains=marca)
        else:
            object_list = self.model.objects.all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BusquedaMonitor()
        return context
    
    
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
