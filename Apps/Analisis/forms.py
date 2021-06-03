from django import forms
from django_select2.forms import ModelSelect2MultipleWidget

from .models import *

class FormFases (forms.ModelForm):
    class Meta:
        model = Fases
        fields = [
            'nombre',
            'estado',
            'fases_previas'
        ]

        widgets = {
            'fases_previas' : ModelSelect2MultipleWidget (
                model = Fases,
                search_fields = ['nombre__icontains'],
                attrs = {
					'class': 'select2_demo_2 form-control',
                    'multiple': 'multiple'
				}
            )
        }

    def __init__(self, *args, **kwargs):
        self.crear = kwargs.pop('crear', None)
        super(FormFases, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormFases, self).clean()
        
        if self.crear:
            try:
                fase = Fases.objects.get(nombre=form_data['nombre'])
                self._errors['nombre'] = ["La fase ya existe"]
            except Fases.DoesNotExist:
                pass
        else:
            try:
                fase = Fases.objects.exclude(nombre=self.instance)
                fase = fase.get(nombre=form_data['nombre'])
                self._errors['nombre'] = ["La fase ya existe"]
            except Fases.DoesNotExist:
                pass

class FormAnalisis (forms.ModelForm):
    class Meta:
        model = Analisis
        fields = [
            'nombre',
            'sigia',
            'estado',
            'unidad_medida',
            'valor_minimo',
            'valor_maximo',
            'fase',
            'iva',
            'tipoIva',
            'precio'
        ]

    def __init__(self, *args, **kwargs):
        self.crear = kwargs.pop('crear', None)
        super(FormAnalisis, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['sigia'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control',
        }
        self.fields['unidad_medida'].widget.attrs = {
            'class': 'form-control',
        }
        self.fields['valor_minimo'].widget.attrs = {
            'class': 'form-control',
            'type':'number',
            'min':'0.00',
        }
        self.fields['valor_maximo'].widget.attrs = {
            'class': 'form-control',
            'type':'number',
            'min':'0.00',
        }
        self.fields['fase'].widget.attrs = {
            'class': 'form-control',
        }
        self.fields['iva'].widget.attrs = {
            'class': 'form-control',
            'type':'number',
            'min':'0.00',
        }
        self.fields['tipoIva'].widget.attrs = {
            'class': 'form-control',
        }
        self.fields['precio'].widget.attrs = {
            'class': 'form-control',
            'type':'number',
            'min':'0.00',
        }

    def clean (self):        
        form_data = super(FormAnalisis, self).clean()
        if self.crear:
            try:
                analisis = Analisis.objects.get(nombre=form_data['nombre'])
                self._errors['nombre'] = ["El análisis de laboratorio ya existe"]
            except Fases.DoesNotExist:
                pass
        else:
            try:
                analisis = Analisis.objects.exclude(nombre=self.instance)
                analisis = analisis.get(nombre=form_data['nombre'])
                self._errors['nombre'] = ["El análisis de laboratorio ya existe"]
            except Fases.DoesNotExist:
                pass

        if form_data['valor_minimo'] > form_data['valor_maximo']:
            self._errors['valor_minimo'] = ["El valor mínimo debe ser menor al valor máximo"]

        if form_data['valor_maximo'] < form_data['valor_minimo']:
            self._errors['valor_maximo'] = ["El valor máximo debe ser superior al valor mínimo"]