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
                    'cliente': 'cliente'
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
                    'cliente': 'cliente'
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

    def clean (self):

        form_data = super(FormRecepcion, self).clean()

        