
from django.http import HttpResponse
from datetime import datetime

from django.template import Template, Context, loader
from primerasvistas.models import Celulares 


def inicio(request):
    return HttpResponse('Bienvenido a la pagina')

def ver_fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'Fecha actual: {fecha_actual}')

def saludo(request, nombre):
    return HttpResponse(f'Hola {nombre}')

def mi_template(request, marca_cel, modelo_cel):
        
    template1 = loader.get_template('prueba.html')
        
    celular = Celulares(marca = marca_cel, modelo = modelo_cel)
    celular.save()
    
    render1 = template1.render({'celular': celular})
   
    return HttpResponse(render1)

def lista_celulares(request):
    
    template = loader.get_template('lista_celulares.html')
    
    lista_celulares = Celulares.objects.all()
    
    render = template.render({'lista_celulares': lista_celulares})
    return HttpResponse(render)
