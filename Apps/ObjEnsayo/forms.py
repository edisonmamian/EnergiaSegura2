from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from django.db.models import fields
from django.forms.models import inlineformset_factory

from .models import *
from .custom_layout_object import *

class FormTiposObjEnsayo (forms.ModelForm):
    class Meta:
        model = TiposObjEnsayo
        fields = {
            'nombre',
            'vidaUtilIndefinida',
            'vidaUtil',
            'estado'
        }

    def __init__(self, *args, **kwargs):
        self.crear = kwargs.pop('crear', None)
        super (FormTiposObjEnsayo, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-9 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('nombre'),
                Field('vidaUtilIndefinida'),
                Field('vidaUtil'),
                Field('estado'),
                HTML("<br>"),
                Fieldset('Agregar análisis',
                    Formset('analisis')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'Registrar')),
                )
            )
                
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['vidaUtilIndefinida'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['vidaUtil'].widget.attrs = {
            'class': 'form-control',
            'type':'number',
            'min':'0.00',
            'value':'10.00'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormTiposObjEnsayo, self).clean()

        if self.crear:
            try:
                tipoObjEnsayo = TiposObjEnsayo.objects.get(nombre=form_data['nombre'])
                self._errors['nombre'] = ["El tipo de objeto de ensayo ya existe"]
            except TiposObjEnsayo.DoesNotExist:
                pass
        else:
            try:
                tipoObjEnsayo = TiposObjEnsayo.objects.exclude(nombre=self.instance)
                tipoObjEnsayo = tipoObjEnsayo.get(nombre=form_data['nombre'])
                self._errors['nombre'] = ["El tipo de cilindro ya existe"]
            except TiposObjEnsayo.DoesNotExist:
                pass

class FormTipoObjEnsayo_Analisis (forms.ModelForm):
    class Meta:
        model = TiposObjEnsayo_Analisis
        fields = [
            'analisis',
            'min_aceptado',
            'max_aceptado',
            'obligatorio'
        ]

    def __init__ (self, *args, **kwargs):
        self.crear = kwargs.pop('crear', None)
        super(FormTipoObjEnsayo_Analisis, self).__init__(*args, **kwargs)

        self.fields['analisis'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['min_aceptado'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['max_aceptado'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['obligatorio'].widget.attrs = {
            'class': 'form-control'
        }

    def clean(self):
        form_data = super(FormTipoObjEnsayo_Analisis, self).clean()
        
        if self.crear:
            try:
                cilindro_analisis = TiposObjEnsayo_Analisis.objects.get(
                    analisis = form_data['analisis'],
                    tipoCilindro = form_data['tipoCilindro']
                )
                self._errors['analisis'] = ["Este análisis ya fue asignado"]
            except TiposObjEnsayo_Analisis.DoesNotExist:
                pass
        else:
            try:
                cilindro_analisis = TiposObjEnsayo_Analisis.objects.exclude(
                    id = self.instance.id
                )

                cilindro_analisis = cilindro_analisis.objects.get(
                    analisis = form_data['analisis'],
                    tipoCilindro = form_data['tipoCilindro']
                )

                self._errors['analisis'] = ["Este análisis ya fue asignado"]
            except TiposObjEnsayo_Analisis.DoesNotExist:
                pass

        if form_data['min_aceptado'] > form_data['max_aceptado']:
            self._errors['min_aceptado'] = ["Este valor debe ser inferior al Valor máximo aceptado"]
            self._errors['max_aceptado'] = ["Este valor debe ser superior al Valor mínimo aceptado"]

FormSet_ObjEnsayo_Analisis = inlineformset_factory(
    TiposObjEnsayo,
    TiposObjEnsayo_Analisis,
    form = FormTipoObjEnsayo_Analisis,
    fields = [
        'analisis',
        'min_aceptado',
        'max_aceptado',
        'obligatorio'
    ],
    extra=1,
    can_delete=True
)