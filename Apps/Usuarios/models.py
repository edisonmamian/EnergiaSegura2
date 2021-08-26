from django.db import models
from django.contrib.auth.models import User, Group

from Apps.comunes.models import TipoIdentificacion, Estado
# Create your models here.

class Usuario (User):
    tipo_documento = models.ForeignKey(
        TipoIdentificacion,
        on_delete=models.CASCADE,
        limit_choices_to={'estado': 1},
        verbose_name='Tipo de identificación'
    )
    num_documento = models.CharField(
        max_length=20,
        verbose_name="Número de documento",
        unique=True
    )
    telefono = models.CharField(
        max_length=20,
        verbose_name="Número telefónico"
    )
    segundo_nombre = models.CharField(
        max_length=100,
        verbose_name="Segundo nombre",
        blank=True
    )
    segundo_apellido = models.CharField(
        max_length=100,
        verbose_name="Segundo apellido",
        blank=True
    )
    rol = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name="Rol"
    )

    def __str__(self):
        return '%s %s' % (self.first_name , self.last_name)

class Roles (Group):
    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        verbose_name='Estado'
    )