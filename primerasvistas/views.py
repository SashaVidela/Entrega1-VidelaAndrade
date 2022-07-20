from django.shortcuts import redirect, render

from .forms import BusquedaCelulares, FormCelulares
from .models import Celulares
from datetime import datetime
from django.contrib.auth.decorators import login_required

def prueba(request):
    return render(request, 'prueba.html')

def crear_celular(request):
    if request.method == 'POST':
        form = FormCelulares(request.POST)
       
        if form.is_valid():
            data = form.cleaned_data
            
            fecha = data.get('fecha_registro')
            if not fecha:
                fecha = datetime.now() 
            
            celular = Celulares(
                marca=data.get('marca'),
                modelo=data.get('modelo'),
                fecha_registro=fecha
            )
            celular.save()
            return redirect('lista_celulares')
        
        else:
            return render(request, 'celulares/crear_celular.html', {'form': form})
        
            
    
    form_celular = FormCelulares()
    
    return render(request, 'celulares/crear_celular.html', {'form': form_celular})


def lista_celulares(request):
                  
    if request.GET:
        
        marcas = request.GET["marca"]
        buscar = Celulares.objects.filter(marca__icontains=marcas)
        
    else:
         
        buscar = ""
         
    return render(request, 'celulares/lista_celulares.html', {'lista_celulares': buscar})


@login_required
def editar_celular(request, id):
    celular = Celulares.objects.get(id=id)
    
    if request.method == 'POST':
        form = FormCelulares(request.POST)
        if form.is_valid():
            celular.marca = form.cleaned_data.get('marca')
            celular.modelo = form.cleaned_data.get('modelo')
            celular.fecha_registro = form.cleaned_data.get('fecha_registro')
            celular.save()
            
            return redirect('lista_celulares')
        
        else:
            return render(request, 'celulares/editar_celular.html', {'form': form, 'celular': celular})
    
      
    form_celular = FormCelulares(initial={'marca': celular.marca, 'modelo': celular.modelo, 'fecha_registro': celular.fecha_registro})
    
    return render(request, 'celulares/editar_celular.html', {'form': form_celular, 'celular': celular})    
     
 
@login_required    
def eliminar_celular(request, id):
    celular = Celulares.objects.get(id=id)
    celular.delete()
    
    return redirect('lista_celulares') 


def mostrar_celular(request, id):
    celular = Celulares.objects.get(id=id)
    return render(request, 'celulares/mostrar_celular.html', {'celular': celular})