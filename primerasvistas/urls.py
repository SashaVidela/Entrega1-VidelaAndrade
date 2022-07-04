from django.urls import path
from .views import inicio, ver_fecha, saludo, mi_template, lista_celulares

urlpatterns = [
    path('', inicio),
    path('fecha/', ver_fecha),
    path('saludo/<nombre>/', saludo),
    path('mi-template', mi_template),
    path('mi-template/<marca_cel>/<modelo_cel>/', mi_template),
    path('lista-celulares/', lista_celulares),
]