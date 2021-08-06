from django.urls import path
from .views import *

app_name = 'comunes'
urlpatterns = [
    path ('tipoIdentificacion/crear/', CrearTipoIdentificacion.as_view(), name = 'crear_tipoIdentificacion'),
    path ('tipoIdentificacion/editar/<int:pk>/', ActualizarTipoIdentificacion.as_view(), name = 'editar_tipoIdentificacion'),
    path ('clasificaciondian/crear/', CrearClasificacionDian.as_view(), name = 'crear_clasificaciondian'),
    path ('clasificaciondian/editar/<int:pk>/', ActualizarClasificacionDian.as_view(), name = 'editar_clasificaciondian'),
    path ('tipocontribuyente/crear/', CrearTipoContribuyente.as_view(), name = 'crear_tipocontribuyente'),
    path ('tipocontribuyente/editar/<int:pk>/', ActualizarTipoContribuyente.as_view(), name = 'editar_tipocontribuyente'),
    path ('actividadeconomica/crear/', CrearActividadEconomica.as_view(), name = 'crear_actividadeconomica'),
    path ('actividadeconomica/editar/<int:pk>/', ActualizarActividadEconomica.as_view(), name = 'editar_actividadeconomica'),
    path ('responsabilidadfiscal/crear/', CrearTiposResponsabilidades.as_view(), name = 'crear_responsabilidadfiscal'),
    path ('responsabilidadfiscal/editar/<int:pk>/', ActualizarTiposResponsabilidades.as_view(), name = 'editar_responsabilidadfiscal'),
    path ('documentoscontables/crear/', CrearDocumentoContableInventario.as_view(), name= 'crear_documentocontable'),
    path ('documentoscontables/editar/<int:pk>/', ActualizarDocumentoContableInventario.as_view(), name='editar_documentocontable')
]