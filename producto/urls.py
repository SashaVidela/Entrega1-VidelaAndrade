from django.urls import path
from . import views
from .views import mostrar_monitor, editar_monitor

urlpatterns = [
    path('monitores/', views.ListaMonitores.as_view(), name = 'lista_monitores'),
    path('crear-monitor/', views.CrearMonitor.as_view(), name = 'crear_monitor'),
    path('editar-monitor/<int:id>/', editar_monitor, name = 'editar_monitor'),
    path('eliminar-monitor/<int:pk>/', views.EliminarMonitor.as_view(), name = 'eliminar_monitor'),
    path('mostrar-monitor/<int:id>/', mostrar_monitor, name = 'mostrar_monitor'),
    
]
