from django import forms
from django_select2.forms import ModelSelect2MultipleWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
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
            'telefono',
            'username',
            'password',
            'rol'
        ]

    
    def __init__ (self, *args, **kwargs):
        self.crear = kwargs.pop('crear', None)
        super (FormUsuario, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Primer nombre'
        self.fields['last_name'].label = 'Primer apellido'
        self.fields['username'].label = 'Usuario'
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['username'].required = True

        self.fields['tipo_documento'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['num_documento'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['first_name'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['segundo_nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['last_name'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['segundo_apellido'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['email'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['telefono'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['username'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['password'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['rol'].widget.attrs = {
            'class': 'form-control'
        }

    def clean(self):
        form_data = super(FormUsuario, self).clean()

        if self.crear:
            try:
                Usuario.objects.get(tipo_documento = form_data['tipo_documento'], num_documento=form_data['num_documento'])
                self._errors['num_documento'] = ['el usuario con este número de documento ya existe']
            except Usuario.DoesNotExist:
                pass

            try:
                Usuario.objects.get(email = form_data['email'])
                self._errors['email'] = ['el usuario con este email ya existe']
            except Usuario.DoesNotExist:
                pass

            try:
                Usuario.objects.get (username = form_data['username'])
                self._errors['username'] = ['el usuario ya existe']
            except Usuario.DoesNotExist:
                pass 
        else:
            try: 
                usuario = Usuario.objects.exclude (username = self.instance.username)
                usuario = usuario.get(tipo_documento = form_data['tipo_documento'], num_documento=form_data['num_documento'])
                self._errors['num_documento'] = ['el usuario con este número de documento ya existe']
            except Usuario.DoesNotExist:
                pass

            try:
                usuario = Usuario.objects.exclude (username = self.instance.username)
                usuario = usuario.get(email = form_data['email'])
                self._errors['email'] = ['el usuario con este email ya existe']
            except Usuario.DoesNotExist:
                pass

            try:
                usuario = Usuario.objects.exclude (username = self.instance.username)
                usuario = usuario.get (username = form_data['username'])
                self._errors['username'] = ['el usuario ya existe']
            except Usuario.DoesNotExist:
                pass 



class FormGrupos (forms.ModelForm):
    class Meta:
        model = Roles 
        fields = [ 
            'name',
            'permissions',
            'estado'
        ]

        widgets = {
            'permissions' : ModelSelect2MultipleWidget(
                model = Permission,
                search_fields = ['name__icontains'],
                attrs = {
                    'class': 'select2_demo_2 form-control',
                    'multiple': 'multiple'
                }
            )
        }

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

class LoginForm (forms.Form):
    username = forms.CharField(
        label = 'Usuario',
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )
    password = forms.CharField(
        label = 'Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        })
    )