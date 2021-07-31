from django.db import models

from Apps.ObjEnsayo.models import TiposObjEnsayo
from Apps.comunes.models import *

# Create your models here.
class ClasificacionClientes (models.Model):
    #almacena el nombre de la clasificación
    nombre = models.CharField(
        max_length=50,
        null=False,
        verbose_name='Nombre'
    )
    #almacena los tipos de cilindros que debería tener el cliente con esta clasificación
    tipos_cilindros = models.ManyToManyField(
        TiposObjEnsayo,
        verbose_name='Tipos de objeto de ensayo',
        limit_choices_to={'estado': 1},
        symmetrical=False,
        blank=True
    )
    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        verbose_name="Estado"
    )

    def __str__(self):
        return self.nombre

# modelo para los clientes de Energia Segura
CONTRIBUYENTE = (
    ('Persona Natural Regimen Simplificado', 'Persona Natural Regimen Simplificado'),
    ('Persona Natural Regimen Comun', 'Persona Natural Regimen Comun'),
    ('Grande Contribuyente Autorretenedor', 'Grande Contribuyente Autorretenedor'),
    ('Grande Contribuyente No Autorretenedor', 'Grande Contribuyente No Autorretenedor'),
    ('Persona Juridica', 'Persona Juridica'),
)
class Clientes (models.Model):
    # almacena el nombre
    nombre = models.CharField(
        max_length=50,
        null=False,
        verbose_name='Nombre o razón social'
    )
    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        verbose_name="Estado"
    )
    # el tipo de identifiación del cliente
    tipo_identifcacion = models.ForeignKey(
        TipoIdentificacion,
        on_delete=models.CASCADE,
        limit_choices_to={'estado': 1},
        verbose_name='Tipo de identificación'
    )
    # el número de identificación del cliente
    numero_identificacion = models.CharField(
        max_length = 10,
        null = False,
        verbose_name = 'Número de identificación'
    )
    # la clasificacion del cliente
    clasificacion = models.ManyToManyField(
        ClasificacionClientes,
        verbose_name = 'Clasificación del cliente',
        limit_choices_to = {'estado': 1}
    )
    contribuyente = models.ForeignKey(
        TipoContribuyente,
        on_delete=models.CASCADE,
        limit_choices_to={'estado': 1},
        verbose_name= 'Tipo de contribuyente'
    )
    plazo = models.IntegerField(
        verbose_name='Plazo para pagos'
    )
    actividadEconomica = models.ForeignKey (
        ActividadEconomica,
        on_delete=models.CASCADE,
        limit_choices_to={'estado': 1},
        verbose_name= 'Actividad Económica'
    )
    tiposResponsabilidades = models.ManyToManyField(
        TiposResponsabilidades,
        limit_choices_to={'estado': 1},
        verbose_name='Tipo de responsabilidad económica'
    )
    documentoContable = models.ForeignKey(
        DocumentosContablesInventarios,
        on_delete=models.CASCADE,
        limit_choices_to={'estado': 1},
        verbose_name= 'Documento contable'
    )

    def __str__(self):
        return self.nombre

    class Meta:
        unique_together = [['tipo_identifcacion', 'numero_identificacion']]

# Modelo de sedes de los clientes
class SedeCliente (models.Model):
    # nombre de la sede
    nombre = models.CharField(
        max_length=50,
        null=False,
        verbose_name='Nombre de la sede'
    )
    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        verbose_name="Estado"
    )
    # departamento en la que está ubicada la sede
    departamento = models.ForeignKey(
        Departamentos,
        on_delete=models.CASCADE,
        verbose_name = 'Departamento'
    )
    # ciudad en la que está ubicada la sede
    ciudad = models.ForeignKey(
        Ciudades,
        on_delete=models.CASCADE,
        verbose_name='Ciudad'
    )
    # dirección de la sede
    direccion = models.CharField(
        max_length = 50,
        null = False,
        verbose_name = 'Dirección'
    )
    # cliente al que pertenece la sede
    cliente = models.ForeignKey(
        Clientes,
        on_delete=models.CASCADE,
        verbose_name='Cliente'
    )
    # el nombre del responsable técnico
    responsable_tecnico = models.CharField(
        max_length = 100,
        verbose_name = 'Nombre del responsable técnico',
        null = True,
        blank = True,
    )
    # el teléfono del responsable técnico
    telefono_tecnico = models.CharField(
        max_length = 20,
        verbose_name = 'Teléfono/celular del responsable técnico',
        null = True,
        blank = True
    )
    # el email del responsable técnico
    email_tecnico = models.EmailField(
        verbose_name = 'Email del responsable técnico',
        null = True,
        blank = True
    )
    # el nombre del responsable comercial
    responsable_comercial = models.CharField(
        max_length = 100,
        verbose_name = 'Nombre del responsable comercial',
        null = True,
        blank = True,
    )
    # el teléfono del responsable comercial
    telefono_comercial = models.CharField(
        max_length = 20,
        verbose_name = 'Teléfono/celular comercial',
        null = True,
        blank = True
    )
    # el email del responsable comercial
    email_comercial = models.EmailField(
        verbose_name = 'Email comercial',
        null = True,
        blank = True
    )
    # el nombre del responsable de contabilidad
    responsable_contabilidad = models.CharField(
        max_length = 100,
        verbose_name = 'Nombre del responsable de contabilidad',
        null = True,
        blank = True,
    )
    # el telefono del responsable de contabilidad
    telefono_contabilidad = models.CharField(
        max_length = 20,
        verbose_name = 'Teléfono/celular de contabilidad',
        null = True,
        blank = True
    )
    # el email del responsable de contabilidad
    email_contabilidad = models.EmailField(
        verbose_name = 'Email de contabilidad',
        null = True,
        blank = True
    )
    # el nombre del responsable administrativo
    responsable_administrativo = models.CharField(
        max_length = 100,
        verbose_name = 'Nombre del responsable administrativo',
        null = True,
        blank = True,
    )
    # el telefono del responsable administrativo
    telefono_administrativo = models.CharField(
        max_length = 20,
        verbose_name = 'Teléfono/celular administrativo',
        null = True,
        blank = True
    )
    # el email del responsable administrativo
    email_administrativo = models.EmailField(
        verbose_name = 'Email administrativo',
        null = True,
        blank = True
    )
    fecha_creacion = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return "%s - %s" %(self.cliente.nombre, self.nombre)