from django.urls import path
from .views import *

app_name = 'ObjEnsayo'
urlpatterns = [
    path ('crear/', CrearObjEnsayo.as_view(), name = 'crear'),
    path ('editar/<int:pk>/', ActualizarObjEnsayo.as_view(), name = 'editar')
]