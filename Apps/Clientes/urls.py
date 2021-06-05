from django.urls import path
from .views import *

app_name = 'Clientes'
urlpatterns = [
    path ('clasificacion/crear/', CrearClasificacion.as_view(), name = 'crear_clasificacion'),
    path ('clasificacion/editar/<int:pk>/', ActualizarClasificacion.as_view(), name = 'editar_clasificacion'),
    #path ('crear/', CrearAnalisis.as_view(), name = 'crear'),
    #path ('editar/<int:pk>/', ActualizarAnalisis.as_view(), name = 'editar')
]