from django.urls import path
from . import views

urlpatterns = [
    path('monitores/', views.ListaMonitores.as_view(), name = 'lista_monitores'),
    path('crear-monitor/', views.CrearMonitor.as_view(), name = 'crear_monitor'),
    path('editar-monitor/<int:pk>/', views.EditarMonitor.as_view(), name = 'editar_monitor'),
    path('eliminar-monitor/<int:pk>/', views.EliminarMonitor.as_view(), name = 'eliminar_monitor'),
    path('mostrar-monitor/<int:pk>/', views.MostrarMonitor.as_view(), name = 'mostrar_monitor'),
]
