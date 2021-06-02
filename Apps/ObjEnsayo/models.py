from django.db import models
from django.core.validators import MinValueValidator

from Apps.comunes.models import Estado
from Apps.Analisis.models import Analisis

# Create your models here.
class TiposObjEnsayo (models.Model):
    nombre = models.CharField(
        max_length=50,
        null=False,
        unique=True,
        verbose_name='Nombre'
    )
    vidaUtil = models.DecimalField(
        max_digits=5,
        decimal_places=3,
        validators=[MinValueValidator(0.0)],
        verbose_name='Vida útil en años',
        null=True,
        blank = True
    )
    vidaUtilIndefinida = models.BooleanField(
        verbose_name = '¿Vida útil indefinida?',
        default = False
    )
    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        verbose_name="Estado"
    )

    class Meta:
        verbose_name = "Tipos de ítem de ensayo"
        ordering = ['nombre', 'estado']

    def __str__(self):
        return self.nombre

class TiposObjEnsayo_Analisis (models.Model):
    tipoObjEnsayo = models.ForeignKey (
        TiposObjEnsayo,
        limit_choices_to = {'estado': 1},
        on_delete=models.CASCADE,
        verbose_name= "Tipo de objeto de Ensayo"
    )
    analisis = models.ForeignKey (
        Analisis,
        limit_choices_to={'estado': 1},
        on_delete=models.CASCADE,
        verbose_name="Análisis de laboratorio"
    )
    min_aceptado = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        verbose_name='Valor mínimo aceptado',
        null=False
    )
    max_aceptado = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        verbose_name='Valor máximo aceptado',
        null=False
    )
    obligatorio = models.BooleanField(
        verbose_name="¿Es obligatorio?",
        default = False,
    )

    class Meta:
        unique_together = [['tipoObjEnsayo', 'analisis']]