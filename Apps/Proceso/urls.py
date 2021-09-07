from django.urls import path
from .views import *

app_name = 'Proceso'
urlpatterns = [
    path ('crear/', Proceso.as_view(), name = 'crear'),
    path ('recepciones/', ListarRecepciones.as_view(), name = 'recepciones'),
    path ('items/<int:pk>/', ListarRecepciones.as_view(), name = 'items')
]