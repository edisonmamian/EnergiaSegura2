from django import forms
from django.contrib.auth.models import Group

from .models import *

class FormUsuario (forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'tipo_documento',
            'num_documento',
            'first_name',
            'segundo_nombre',
            'last_name',
            'segundo_apellido',
            'email',
            'telefono'
        ]

class FormGrupos (forms.ModelForm):
    class Meta:
        model = Roles 
        fields = [ 
            'name',
            'permissions',
            'estado'
        ]

    def __init__ (self, *args, **kwargs):
        self.crear = kwargs.pop('crear', None)
        super (FormGrupos, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Rol'
        self.fields['permissions'].label = 'Permisos'

        self.fields['permissions'].widget.attrs = {
            'class': 'form-control'
        }

        self.fields['name'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormGrupos, self).clean()

        if self.crear:
            try:
                rol = Roles.objects.get(name = form_data['name'])
                self._errors['name'] = ['El rol ya existe']
            except Roles.DoesNotExist:
                pass
        else:
            try:
                rol = Roles.objects.exclude(name = self.instance)
                rol = rol.get(name = form_data['name'])
                self._errors['nombre'] = ['El rol ya existe']
            except Roles.DoesNotExist:
                pass 

