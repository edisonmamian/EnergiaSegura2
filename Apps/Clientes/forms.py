from django import forms
from django_select2.forms import ModelSelect2MultipleWidget, ModelSelect2Widget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from django.forms.models import inlineformset_factory

from .models import *
from .custom_layout_object import *
from Apps.ObjEnsayo.models import TiposObjEnsayo
from Apps.comunes.models import Departamentos, Ciudades

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

        return form_data

class FormCliente (forms.ModelForm):
    class Meta:
        model = Clientes
        fields = [
            'nombre',
            'estado',
            'tipo_identifcacion',
            'numero_identificacion',
            'clasificacion',
            'contribuyente',
            'plazo',
            'actividadEconomica',
            'tiposResponsabilidades',
            'documentoContable'
        ]
        widgets = {
            'clasificacion' : ModelSelect2MultipleWidget (
                model = TiposObjEnsayo,
                search_fields = ['nombre__icontains'],
                attrs = {
					'class': 'select2_demo_2 form-control',
                    'multiple': 'multiple'
				}
            ),
            'tiposResponsabilidades' : ModelSelect2MultipleWidget (
                model = TiposResponsabilidades,
                search_fields = ['nombre__icontains'],
                attrs = {
					'class': 'select2_demo_2 form-control',
                    'multiple': 'multiple'
				}
            )
        }   

    def __init__(self, *args, **kwargs):
        self.crear = kwargs.pop('crear', None)
        super(FormCliente, self).__init__(*args, **kwargs)

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
                        Field('estado', css_class='form form-control'),
                        css_class = 'col-lg-6'
                    ),
                    css_class = ' row'
                ),
                Div(
                    Div(
                        Field('tipo_identifcacion', css_class='form form-control'),
                        css_class = 'col-lg-6'
                    ),
                    Div(
                        Field('numero_identificacion', css_class='form form-control '),
                        css_class = 'col-lg-6'
                    ),
                    css_class = 'row'
                ), 
                Div(
                    Div(
                        Field('clasificacion', css_class='form form-control'),
                        css_class = 'col-lg-6'
                    ),
                    Div(
                        Field('contribuyente', css_class='form form-control '),
                        css_class = 'col-lg-6'
                    ),
                    css_class = 'row'
                ), 
                Div(
                    Div(
                        Field('plazo', css_class='form form-control'),
                        css_class = 'col-lg-6'
                    ),
                    Div(
                        Field('tiposResponsabilidades'),
                        css_class = 'col-lg-6'
                    ),
                    css_class = 'row'
                ),   
                Div(
                    Div(
                        Field('actividadEconomica', css_class='form form-control'),
                        css_class = 'col-lg-6'
                    ),
                    Div(
                        Field('documentoContable', css_class='form form-control'),
                        css_class = 'col-lg-6'
                    ),
                    css_class = 'row'
                ),              
                HTML("<br>"),
                Fieldset('Agregar sede',
                    Formset('cliente')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', boton)),
                )
            )


        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['tipo_identifcacion'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['numero_identificacion'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['contribuyente'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['plazo'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['actividadEconomica'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['documentoContable'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormCliente, self).clean()

        if self.crear:
            try:
                cliente = Clientes.objects.get(
                    tipo_identifcacion = form_data['tipo_identifcacion'],
                    numero_identificacion = form_data['numero_identificacion']
                )
                self._errors['nombre'] = ['La clasificación de clientes ya existe']
            except Clientes.DoesNotExist:
                pass
        else:
            try:
                cliente = Clientes.objects.exclude(nombre = self.instance)
                cliente = cliente.get(
                    tipo_identifcacion = form_data['tipo_identifcacion'],
                    numero_identificacion = form_data['numero_identificacion']
                )
            except Clientes.DoesNotExist:
                pass

        if form_data['plazo'] < 0:
            self._errors['plazo'] = ['El plazo de pago no puede se inferior a cero días']
        
        return form_data

class FormSede (forms.ModelForm):
    class Meta:
        model = SedeCliente
        fields = [
            'nombre',
            'estado',
            'departamento',
            'ciudad',
            'direccion',
            'responsable_tecnico',
            'telefono_tecnico',
            'email_tecnico',
            'responsable_comercial',
            'telefono_comercial',
            'email_comercial',
            'responsable_contabilidad',
            'telefono_contabilidad',
            'email_contabilidad',
            'responsable_administrativo',
            'telefono_administrativo',
            'email_administrativo'
        ]
        widgets = {
            'departamento' : ModelSelect2Widget (
                model = Departamentos,
                search_fields = ['nombre__icontains'],
                attrs = {
                    'class': 'select2_demo_2 form-control'
                }
            ),
            'ciudad' : ModelSelect2Widget (
                model = Ciudades,
                search_fields = ['nombre__icontains'],
                dependent_fields = {
                    'departamento': 'departamento'
                },
                attrs = {
                    'class': 'select2_demo_2 form-control'
                }
            )
        }

    def __init__(self, *args, **kwargs):
        self.crear = kwargs.pop('crear', None)
        super(FormSede, self).__init__(*args, **kwargs)

        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['direccion'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['responsable_tecnico'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['telefono_tecnico'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['email_tecnico'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['responsable_comercial'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['telefono_comercial'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['email_comercial'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['responsable_contabilidad'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['telefono_contabilidad'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['email_contabilidad'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['responsable_administrativo'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['telefono_administrativo'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['email_administrativo'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormCliente, self).clean()

        if self.crear:
            try:
                SedeCliente.objects.get(
                    cliente=form_data['cliente'],
                    nombre = form_data['nombre']
                )
                self.__error ['nombre'] = ['La sede ya existe']
            except SedeCliente.DoesNotExist:
                pass
        else:
            try:
                sede = SedeCliente.objects.exclude(nombre = self.instance)
                sede.get(
                    cliente=form_data['cliente'],
                    nombre = form_data['nombre']
                )
                self.__error ['nombre'] = ['La sede ya existe']
            except SedeCliente.DoesNotExist:
                pass

        return form_data

FormSet_Clientes_Sedes = inlineformset_factory(
    Clientes,
    SedeCliente,
    form = FormSede,
    fields = [
        'nombre',
        'estado',
        'departamento',
        'ciudad',
        'direccion',
        'responsable_tecnico',
        'telefono_tecnico',
        'email_tecnico',
        'responsable_comercial',
        'telefono_comercial',
        'email_comercial',
        'responsable_contabilidad',
        'telefono_contabilidad',
        'email_contabilidad',
        'responsable_administrativo',
        'telefono_administrativo',
        'email_administrativo'
    ],
    extra=1,
    can_delete=True
)