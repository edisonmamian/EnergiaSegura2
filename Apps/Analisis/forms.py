from django import forms
from django_select2.forms import ModelSelect2MultipleWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from django.forms.models import inlineformset_factory

from .models import *
from .custom_layout_object import *

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
        
        return form_data

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
            'precio',
            'frecuencia',
            'opcionesAlternativas'
        ]

    def __init__(self, *args, **kwargs):
        self.crear = kwargs.pop('crear', None)
        super(FormAnalisis, self).__init__(*args, **kwargs)

        if self.crear:
            boton = 'Registrar'
        else:
            boton = 'Actualizar'


        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-9 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div(
                        Field('nombre', css_class='form form-control'),
                        css_class = 'col-lg-6'
                    ),
                    Div(
                        Field('sigia', css_class='form form-control'),
                        css_class = 'col-lg-6'
                    ),
                    css_class = "row"
                ),
                Div(
                    Div(
                        Field('estado', css_class='form form-control'),
                        css_class = 'col-lg-6'
                    ),
                    Div(
                        Field('frecuencia', css_class='form form-control'),
                        css_class = 'col-lg-6'
                    ),
                    css_class = "row"
                ),
                Div(
                    Div(
                        Field('fase', css_class='form form-control'),
                        css_class = 'col-lg-6'
                    ),
                    Div(
                        Field('iva', css_class='form form-control'),
                        css_class = 'col-lg-6'
                    ),
                    css_class = "row"
                ), 
                Div(
                    Div(
                        Field('tipoIva', css_class='form form-control'),
                        css_class = 'col-lg-6'
                    ),
                    Div(
                        Field('precio', css_class='form form-control'),
                        css_class = 'col-lg-6'
                    ),
                    css_class = "row"
                ),
                Div(                    
                    Div(
                        Field('opcionesAlternativas', css_class='form form-control'),
                        css_class = 'col-lg-6'
                    ),                    
                    Div(
                        Field('unidad_medida', css_class='form form-control'),
                        css_class = 'col-lg-6'
                    ),
                    css_class = "row"
                ),  
                Div(
                    Div(
                        Field('valor_minimo', css_class='form form-control'),
                        css_class = 'col-lg-6'
                    ),
                    Div(
                        Field('valor_maximo', css_class='form form-control'),
                        css_class = 'col-lg-6'
                    ),
                    css_class = "row"
                ),        
                HTML("<br>"),
                Fieldset('Agregar valor alternativo',
                    Formset('valalt')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', boton)),
                css_class = "formset-valalt" 
            )
        )

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
            'type':'number'
        }
        self.fields['valor_maximo'].widget.attrs = {
            'class': 'form-control',
            'type':'number'
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
        self.fields['frecuencia'].widget.attrs = {
            'class': 'form-control',
        }
        self.fields['opcionesAlternativas'].widget.attrs = {
            'class': 'form-control',
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

        if not form_data['opcionesAlternativas']:
            min_val = form_data['valor_minimo']
            max_val = form_data['valor_maximo']
            if  min_val != None and max_val != None:
                if min_val > max_val:
                    self._errors['valor_minimo'] = ["El valor mínimo debe ser menor al valor máximo"]
                    self._errors['valor_maximo'] = ["El valor máximo debe ser superior al valor mínimo"]
            else:
                if min_val == None:                    
                    self._errors['valor_minimo'] = ['El valor mínimo no puede estar vacío']

                if max_val == None:
                    self._errors['valor_maximo'] = ["El valor máximo no puede estar vacío"]    

        return form_data

class FormValoresAlternativos (forms.ModelForm):
    class Meta:
        model = ValoresAlternativos
        fields =  [
            'nombre',
            'aprueba'
        ]

    def __init__(self, *args, **kwargs):
        self.crear = kwargs.pop('crear', None)
        super(FormValoresAlternativos, self).__init__(*args, **kwargs)

        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['aprueba'].widget.attrs = {
            'class': 'form-control'
        }

FormSet_Analisis_ValAlter = inlineformset_factory(
    Analisis,
    ValoresAlternativos,
    form = FormValoresAlternativos,
    fields =  [
        'nombre',
        'aprueba'
    ],
    extra=1,
    can_delete=True
)