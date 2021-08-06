from django.urls import path
from .views import *

app_name = 'Analisis'
urlpatterns = [
    # este es un ejemplo para ver 
    path ('fases/crear/', CrearFase.as_view(), name = 'crear_fase'),
    path ('fases/editar/<int:pk>/', ActualizarFase.as_view(), name = 'editar_fase'),
    path ('crear/', CrearAnalisis.as_view(), name = 'crear'),
    path ('editar/<int:pk>/', ActualizarAnalisis.as_view(), name = 'editar')
]