from django.db import models
from Apps.Analisis.models import Analisis, ValoresAlternativos
from Apps.Usuarios.models import Usuario
# Create your models here.

class Proceso (models.Model):
    analisis = models.ForeignKey(
        Analisis,
        on_delete=models.CASCADE,
        verbose_name='Análisis'
    )
    valoresAlternativos = models.ForeignKey(
        ValoresAlternativos,
        on_delete=models.CASCADE,
        verbose_name="Valores Alternativos"
    )
    valor = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        verbose_name='Resultado',
        null=True
    )
    colaborador = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        verbose_name="Colaborador responsable"
    )

