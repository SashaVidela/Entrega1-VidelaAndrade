
from django.http import HttpResponse
from datetime import datetime

from django.template import Template


def inicio(request):
    return HttpResponse('Hola soy mi primer vista en django')

def ver_fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'Fecha actual: {fecha_actual}')

def saludo(request, nombre):
    return HttpResponse(f'Hola {nombre}')

def mi_template(request):
    
    archivo = open(r'C:\Users\54115\Desktop\Proyecto_Intermedio+VidelaAndrade\templates\prueba.html', 'r')
    
   Template
   
    return HttpResponse('Mi template')