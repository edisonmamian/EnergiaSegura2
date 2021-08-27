from django.urls import path
from .views import *

app_name = 'usuarios'
urlpatterns = [
    path ('roles/crear/', CrearRoles.as_view(), name='roles_crear'),    
    path ('roles/editar/<int:pk>/', EditarRoles.as_view(), name = 'roles_editar'),
    path ('usuarios/crear/', CrearUsuario.as_view(), name='usuarios_crear'), 
    path ('usuarios/editar/<int:pk>/', EditarUsuario.as_view(), name = 'usuarios_editar'),
    path ('login/', LoginUsuario.as_view(), name = 'login'),
    path ('logout/', LogoutUsuario, name = 'logout'),
]