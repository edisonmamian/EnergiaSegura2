from django.db import models

# Create your models here.
class Estado (models.Model):
    nombre = models.CharField (
        max_length = 20,
        null = False,
        unique = True,
        verbose_name = 'Estado'
    )

class TipoIdentificacion (models.Model):
    nombre = models.CharField (
        max_length = 20,
        null = False,
        unique = True,
        verbose_name = 'Tipo Identificación'
    )
    estado = models.ForeignKey (
        Estado,
        limit_choices_to={'nombre': 'Activo'},
        on_delete=models.CASCADE,
        verbose_name='Estado'
    )