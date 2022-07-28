from django.shortcuts import redirect, render
from .forms import FormMonitores

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import BusquedaMonitor
from .models import Monitores


class ListaMonitores(ListView):
    model = Monitores
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
    
    
    
def editar_monitor(request, id):
    monitor = Monitores.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormMonitores(request.POST)
        if form.is_valid():
            monitor.marca = form.cleaned_data.get('marca')
            monitor.modelo = form.cleaned_data.get('modelo')
            monitor.precio = form.cleaned_data.get('precio')
            monitor.descripcion = form.cleaned_data.get('descripcion')
            monitor.avatars = form.cleaned_data.get('avatars')                       
            monitor.save()
            
            return redirect('lista_monitores')
        
        else:
            return render(request, 'monitores/editar_monitor.html', {'form': form, 'monitor': monitor})
    
    form_monitor = FormMonitores(
        initial={
            'marca': monitor.marca,
            'modelo': monitor.modelo,
            'precio': monitor.precio,
            'descripcion': monitor.descripcion,
            'avatars': monitor.avatars                      
            }
        )
    
    return render(request, 'monitores/editar_monitor.html', {'form': form_monitor, 'monitor': monitor}) 
    



class EliminarMonitor(LoginRequiredMixin, DeleteView):
    model=Monitores
    template_name = 'monitores/eliminar_monitor.html'
    success_url = '/producto/monitores'



def mostrar_monitor(request, id):
    monitor = Monitores.objects.get(id=id)
    return render(request, 'monitores/mostrar_monitor.html', {'monitor': monitor})