from Apps.comunes.models import Estado
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Fases (models.Model):
    nombre = models.CharField(
        max_length=50,
        null=False,
        unique=True,
        verbose_name='Nombre'
    )
    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        verbose_name="Estado"
    )
    fases_previas = models.ManyToManyField(
        'self',
        related_name='previa',
        verbose_name='Fases previas',
        limit_choices_to={'estado': 1},
        symmetrical=False,
        blank=True
    )

    class Meta:
        verbose_name = "Fases"
        ordering = ['nombre', 'estado']

    def __str__(self):
        return self.nombre

tiposIVA = (
    ('Gravado', 'Gravado'),
    ('Exento', 'Exento'),
    ('Excluido', 'Excluido'),
    ('AIU Gravado', 'AIU Gravado'),
    ('AIU No Gravado', 'AIU No Gravado'),
    ('No Gravados', 'No Gravados')
)

class Analisis (models.Model):
    nombre = models.CharField(
        max_length=100,
        null=False,
        unique=True,
        verbose_name='Nombre'
    )
    sigia = models.CharField(
        max_length=100,
        null=False,
        unique=True,
        verbose_name='Sigia'
    )
    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        verbose_name="Estado"
    )
    unidad_medida = models.CharField(
        max_length=20,
        null=False,
        verbose_name='Unidad de medida'
    )
    valor_minimo = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        verbose_name='Valor mínimo',
        null=False
    )
    valor_maximo = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        verbose_name='Valor maximo',
        null=False
    )
    fase = models.ForeignKey(
        Fases,
        limit_choices_to={'estado': 1},
        on_delete=models.CASCADE,
        verbose_name="Fase"
    )
    iva = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        verbose_name= 'IVA',
        null = False
    )
    tipoIva = models.CharField (
        max_length=20,
        choices=tiposIVA,
        null=False,
        verbose_name='Tipo de iva'
    )
    precio = models.DecimalField (
        max_digits=10,
        decimal_places=2,
        verbose_name='Precio de venta',
        null=False
    )

    class Meta:
        verbose_name = "Análisis"
        ordering = ['nombre', 'estado']

    def __str__(self):
        return self.nombre