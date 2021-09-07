from django import forms

from .models import *

class FormProceso (forms.ModelForm):
    class Meta:
        model = Proceso
        fields = [ 
            'analisis',
            'valoresAlternativos',
            'valor',
            'colaborador'
        ]