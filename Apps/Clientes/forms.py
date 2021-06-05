from django import forms
from django.db.models import fields
from django_select2.forms import ModelSelect2MultipleWidget, ModelSelect2Widget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from django.forms.models import inlineformset_factory

from .models import *
from Apps.ObjEnsayo.models import TiposObjEnsayo

class FormClasificacion (forms.ModelForm):
    class Meta:
        model = ClasificacionClientes
        fields = [
            'nombre',
            'tipos_cilindros',
            'estado'
        ]

        widgets = {
            'tipos_cilindros' : ModelSelect2MultipleWidget (
                model = TiposObjEnsayo,
                search_fields = ['nombre__icontains'],
                attrs = {
					'class': 'select2_demo_2 form-control',
                    'multiple': 'multiple'
				}
            )
        }

    def __init__(self, *args, **kwargs):
        self.crear = kwargs.pop('crear', None)
        super(FormClasificacion, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormClasificacion, self).clean()

        if self.crear:
            try:
                clasificacion = ClasificacionClientes.objects.get(nombre = form_data['nombre'])
                self._errors['nombre'] = ['La clasificación de clientes ya existe']
            except ClasificacionClientes.DoesNotExist:
                pass
        else:
            try:
                clasificacion = ClasificacionClientes.objects.exclude(nombre = self.instance)
                clasificacion = clasificacion.get(nombre = form_data['nombre'])
            except ClasificacionClientes.DoesNotExist:
                pass