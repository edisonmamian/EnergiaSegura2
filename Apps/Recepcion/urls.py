from django.urls import path
from .views import *

app_name = 'Recepcion'
urlpatterns = [
    path ('crear/', CrearRecepcion.as_view(), name = 'crear'),
    path ('editar/<int:pk>/', ActualizarRecepcion.as_view(), name = 'editar')
]