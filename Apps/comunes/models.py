from django.db import models

# Create your models here.
class Estado (models.Model):
    nombre = models.CharField (
        max_length = 20,
        null = False,
        unique = True,
        verbose_name = 'Estado'
    )

    def __str__(self):
        return self.nombre

class TipoIdentificacion (models.Model):
    nombre = models.CharField (
        max_length = 20,
        null = False,
        unique = True,
        verbose_name = 'Tipo Identificación'
    )
    estado = models.ForeignKey (
        Estado,
        on_delete=models.CASCADE,
        verbose_name='Estado'
    )

    def __str__(self):
        return self.nombre

class Departamentos (models.Model):
    #Almacena el nombre del departamento
    nombre = models.CharField(
        max_length = 20,
        null = False,
        unique = True,
        verbose_name = 'Departamento'
    )
    #Almacena el código de identificación del departamento
    codigo_dane = models.CharField(
        max_length = 2,
        null = False,
        unique = True,
        verbose_name = 'Código DANE'
    )

    def __str__(self):
        return self.nombre

#modelo para las ciudades de Colombia
class Ciudades (models.Model):
    #Almacena el nombre de la ciudad
    nombre = models.CharField(
        max_length = 20,
        null = False,
        verbose_name = 'Ciudad'
    )
    #Almacena el departamento en el que está ubicado
    departamento = models.ForeignKey(
        Departamentos,
        on_delete=models.CASCADE,
        verbose_name = 'Departamento'
    )
    #Almacena el código de identificación de la ciudad
    codigo_dane = models.CharField (
        max_length = 5,
        unique = True,
        verbose_name = 'Código DANE'
    )

    def __str__(self):
        return self.nombre

class ClasificacionDian (models.Model):
    nombre = models.CharField(
        max_length = 50,
        null = False,
        verbose_name = 'Clasificación DIAN'
    )
    estado = models.ForeignKey (
        Estado,
        on_delete=models.CASCADE,
        verbose_name='Estado'
    )

    def __str__(self):
        return self.nombre

class TipoContribuyente (models.Model):
    nombre = models.CharField(
        max_length = 50,
        null = False,
        verbose_name = 'Clasificación DIAN'
    )
    estado = models.ForeignKey (
        Estado,
        on_delete=models.CASCADE,
        verbose_name='Estado'
    )

    def __str__(self):
        return self.nombre

class ActividadEconomica (models.Model):
    nombre = models.CharField(
        max_length= 50,
        null = False,
        verbose_name='Actividad económica'
    )
    codigo = models.CharField(
        max_length=50,
        null=False,
        verbose_name='Código de la actividad económica'
    )
    estado = models.ForeignKey (
        Estado,
        on_delete=models.CASCADE,
        verbose_name='Estado'
    )

    def __str__(self):
        return self.nombre

class TiposResponsabilidades (models.Model):
    nombre = models.CharField(
        max_length= 50,
        null = False,
        verbose_name='Responsabilidad'
    )
    codigo = models.CharField(
        max_length=50,
        null=False,
        verbose_name='Código de responsabilidades'
    )
    estado = models.ForeignKey (
        Estado,
        on_delete=models.CASCADE,
        verbose_name='Estado'
    )

    def __str__(self):
        return self.nombre