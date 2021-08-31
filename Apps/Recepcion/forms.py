from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from django.forms.models import inlineformset_factory
from django_select2.forms import ModelSelect2Widget

from .models import *
from .custom_layout_object import *

class FormRecepcion (forms.ModelForm):
    class Meta:
        model = Recepcion
        fields = [
            'cliente_factura',
            'sede_cliente_factura',
            'cliente_informe',
            'sede_cliente_informe',
            'fecha',
            'colaborador'
        ]
        widgets = {
            'cliente_factura' : ModelSelect2Widget (
                model = Clientes,
                search_fields = ['nombre__icontains'],
                attrs = {
                    'class': 'select2_demo_2 form-control'
                }
            ),
            'sede_cliente_factura' : ModelSelect2Widget (
                model = SedeCliente,
                search_fields = ['nombre__icontains'],
                dependent_fields = {
                    'cliente_factura': 'cliente_factura'
                },
                attrs = {
                    'class': 'select2_demo_2 form-control'
                }
            ),
            'cliente_informe' : ModelSelect2Widget (
                model = Clientes,
                search_fields = ['nombre__icontains'],
                attrs = {
                    'class': 'select2_demo_2 form-control'
                }
            ),
            'sede_cliente_informe' : ModelSelect2Widget (
                model = SedeCliente,
                search_fields = ['nombre__icontains'],
                dependent_fields = {
                    'cliente_informe': 'cliente_informe'
                },
                attrs = {
                    'class': 'select2_demo_2 form-control'
                }
            )
        }

    def __init__(self, *args, **kwargs):
        self.crear = kwargs.pop('crear', None)
        super (FormRecepcion, self).__init__(*args, **kwargs)

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
                        Field('cliente_factura', css_class='form form-control'),
                        css_class = 'col-lg-6'
                    ),
                    Div(  
                        Field('sede_cliente_factura', css_class='form form-control'),
                        css_class = 'col-lg-6'
                    ),
                    css_class = ' row'
                ),
                Div(
                    Div(
                        Field('cliente_informe', css_class='form form-control'),
                        css_class = 'col-lg-6'
                    ),
                    Div(
                        Field('sede_cliente_informe', css_class='form form-control '),
                        css_class = 'col-lg-6'
                    ),
                    css_class = 'row'
                ), 
                Div(
                    Div(
                        Field('fecha', css_class='form form-control'),
                        css_class = 'col-lg-6'
                    ),
                    Div(
                        Field('colaborador', css_class='form form-control '),
                        css_class = 'col-lg-6'
                    ),
                    css_class = 'row'
                ),            
                HTML("<br>"),
                Fieldset('Agregar item',
                    Formset('itemRecibido')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', boton)),
                )
            )


    def clean (self):
        form_data = super(FormRecepcion, self).clean()

        return form_data

class FormItemRecibido (forms.ModelForm):
    class Meta:
        model = ItemRecibido
        fields = [ 
            'gas',
            'fabricante',
            'serial',
            'analisis',
            'accesorio',
            'capacidad',
            'valvula'
        ]
    
    def __init__ (self, *args, **kwargs):
        self.crear = kwargs.pop('crear', None)
        super(FormItemRecibido, self).__init__(*args, **kwargs)
        self.fields['gas'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['fabricante'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['serial'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['analisis'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['accesorio'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['capacidad'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['valvula'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormItemRecibido, self).clean()
        gas = form_data['gas']
        fabricante = form_data['fabricante']
        accesorio = form_data['accesorio']
        valvula = form_data['valvula']

        if (gas == None or gas == '') and (fabricante == None or fabricante == ''):
            self._errors['gas'] = ["El campo gas o fabricante deben estar diligenciados"]
            self._errors['fabricante'] = ["El campo gas o fabricante deben estar diligenciados"]

        if (accesorio == None or accesorio == '') and (valvula == None or valvula == ''):
            self._errors['accesorio'] = ["El campo accesorio o valvula deben estar diligenciados"]
            self._errors['valvula'] = ["El campo accesorio o valvula deben estar diligenciados"]

        return form_data

Formset_Recepcion_ItemRecibido = inlineformset_factory(
    Recepcion,
    ItemRecibido,
    form = FormItemRecibido,
    fields = [ 
        'gas',
        'fabricante',
        'serial',
        'analisis',
        'accesorio',
        'capacidad',
        'valvula'
    ],
    extra=1,
    can_delete=True
)