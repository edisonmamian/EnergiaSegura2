
from django.db import models

from Apps.Clientes.models import Clientes, SedeCliente
from Apps.Usuarios.models import Usuario
from Apps.Analisis.models import Analisis

# Create your models here.
class Recepcion(models.Model):
    cliente_factura = models.ForeignKey(
        Clientes,
        on_delete=models.CASCADE,
        limit_choices_to={'estado': 1},
        verbose_name='Cliente al que se factura',
        related_name='facturar'
    )
    sede_cliente_factura = models.ForeignKey(
        SedeCliente,
        on_delete= models.CASCADE,
        limit_choices_to={'estado': 1},
        verbose_name='Sede del cliente al que se le factura',
        related_name='facturar'
    )
    cliente_informe = models.ForeignKey(
        Clientes,
        on_delete=models.CASCADE,
        limit_choices_to={'estado': 1},
        verbose_name='Cliente al que se dirige el informe',
        related_name='informe'
    )
    sede_cliente_informe = models.ForeignKey(
        SedeCliente,
        on_delete=models.CASCADE,
        limit_choices_to={'estado': 1},
        verbose_name='Sede del cliente al que se le dirige el informe',
        related_name='informe'
    )
    fecha = models.DateField(
        null = False,
        blank = False,
        verbose_name = 'Fecha de recepción'
    )
    colaborador = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        limit_choices_to={'is_active': True},
        verbose_name='Colaborador que recibe'
    )

class ItemRecibido (models.Model):
    recepcion = models.ForeignKey (
        Recepcion,
        on_delete=models.CASCADE,
        verbose_name='Recepcion'
    )
    gas = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='Gas'
    )
    fabricante = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='Fabricante'
    )
    serial = models.CharField(
        max_length=50,
        null = False,
        verbose_name='Serial'
    )
    analisis = models.ManyToManyField(
        Analisis,
        verbose_name='Servicios'
    )
    accesorio = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Accesorios'
    )
    capacidad = models.CharField(
        max_length=5,
        null=True,
        blank=True,
        verbose_name='Capacidad'
    )
    valvula = models.CharField(
        max_length=50,
        null=False,
        verbose_name='Valvula'
    )