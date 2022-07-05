from django.urls import path
from .views import prueba, crear_celular, lista_celulares

urlpatterns = [
    path('', prueba, name = 'index'),
    path('celulares/', lista_celulares, name = 'lista_celulares'),
    path('crear-celular/', crear_celular, name = 'crear_celular'),
]