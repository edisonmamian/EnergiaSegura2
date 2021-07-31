from django import forms

from .models import *

class FormTipoIdentificacion (forms.ModelForm):
    class Meta:
        model = TipoIdentificacion
        fields = [
            'nombre',
            'estado'
        ]

    def __init__(self, *args, **kwargs):
        self.crear = kwargs.pop('crear', None)
        super(FormTipoIdentificacion, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormTipoIdentificacion, self).clean()

        if self.crear:
            try:
                clasificacion = TipoIdentificacion.objects.get(nombre = form_data['nombre'])
                self._errors['nombre'] = ['El tipo de identificación ya existe']
            except TipoIdentificacion.DoesNotExist:
                pass
        else:
            try:
                clasificacion = TipoIdentificacion.objects.exclude(nombre = self.instance)
                clasificacion = clasificacion.get(nombre = form_data['nombre'])
                self._errors['nombre'] = ['El tipo de identificación ya existe']
            except TipoIdentificacion.DoesNotExist:
                pass

class FormClasificacionDian (forms.ModelForm):
    class Meta:
        model = ClasificacionDian
        fields = [
            'nombre',
            'estado'
        ]

    def __init__(self, *args, **kwargs):
        self.crear = kwargs.pop('crear', None)
        super(FormClasificacionDian, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormClasificacionDian, self).clean()

        if self.crear:
            try:
                clasificacion = ClasificacionDian.objects.get(nombre = form_data['nombre'])
                self._errors['nombre'] = ['La clasificación DIAN ya existe']
            except ClasificacionDian.DoesNotExist:
                pass
        else:
            try:
                clasificacion = ClasificacionDian.objects.exclude(nombre = self.instance)
                clasificacion = clasificacion.get(nombre = form_data['nombre'])
                self._errors['nombre'] = ['La clasificación DIAN ya existe']
            except ClasificacionDian.DoesNotExist:
                pass 

class FormTipoContribuyente (forms.ModelForm):
    class Meta:
        model = TipoContribuyente
        fields = [
            'nombre',
            'estado'
        ]

    def __init__(self, *args, **kwargs):
        self.crear = kwargs.pop('crear', None)
        super(FormTipoContribuyente, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormTipoContribuyente, self).clean()

        if self.crear:
            try:
                clasificacion = TipoContribuyente.objects.get(nombre = form_data['nombre'])
                self._errors['nombre'] = ['Tipo de contribuyente ya existe']
            except TipoContribuyente.DoesNotExist:
                pass
        else:
            try:
                clasificacion = TipoContribuyente.objects.exclude(nombre = self.instance)
                clasificacion = clasificacion.get(nombre = form_data['nombre'])
                self._errors['nombre'] = ['Tipo de contribuyente ya existe']
            except TipoContribuyente.DoesNotExist:
                pass 

class FormActividadEconomica (forms.ModelForm):
    class Meta:
        model = ActividadEconomica
        fields = [
            'nombre',
            'codigo',
            'estado'
        ]

    def __init__(self, *args, **kwargs):
        self.crear = kwargs.pop('crear', None)
        super(FormActividadEconomica, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['codigo'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormActividadEconomica, self).clean()

        if self.crear:
            try:
                clasificacion = ActividadEconomica.objects.get(codigo = form_data['codigo'])
                self._errors['codigo'] = ['La actividad económica ya existe']
            except ActividadEconomica.DoesNotExist:
                pass
        else:
            try:
                clasificacion = ActividadEconomica.objects.exclude(nombre = self.instance)
                clasificacion = clasificacion.get(codigo = form_data['codigo'])
                self._errors['codigo'] = ['La actividad económica ya existe']
            except ActividadEconomica.DoesNotExist:
                pass 

class FormTiposResponsabilidades (forms.ModelForm):
    class Meta:
        model = TiposResponsabilidades
        fields = [
            'nombre',
            'codigo',
            'estado'
        ]

    def __init__(self, *args, **kwargs):
        self.crear = kwargs.pop('crear', None)
        super(FormTiposResponsabilidades, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['codigo'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormTiposResponsabilidades, self).clean()

        if self.crear:
            try:
                clasificacion = TiposResponsabilidades.objects.get(codigo = form_data['codigo'])
                self._errors['codigo'] = ['La responsabilidad ya existe']
            except TiposResponsabilidades.DoesNotExist:
                pass
        else:
            try:
                clasificacion = TiposResponsabilidades.objects.exclude(nombre = self.instance)
                clasificacion = clasificacion.get(codigo = form_data['codigo'])
                self._errors['codigo'] = ['La responsabilidad ya existe']
            except TiposResponsabilidades.DoesNotExist:
                pass 

class FormDocumentosContablesInventarios (forms.ModelForm):
    class Meta:
        model = DocumentosContablesInventarios
        fields = [
            'abreviacion',
            'documentoContable',
            'estado'
        ]

    def __init__(self, *args, **kwargs):
        self.crear = kwargs.pop('crear', None)
        super(FormDocumentosContablesInventarios, self).__init__(*args, **kwargs)
        self.fields['abreviacion'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['documentoContable'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['estado'].widget.attrs = {
            'class': 'form-control'
        }

    def clean (self):
        form_data = super(FormDocumentosContablesInventarios, self).clean()

        if self.crear:
            try:
                abreviacion = DocumentosContablesInventarios.objects.get(abreviacion = form_data['abreviacion'])
                self._errors['abreviacion'] = ['El documento contable ya existe']
            except DocumentosContablesInventarios.DoesNotExist:
                pass
        else:
            try:
                abreviacion = DocumentosContablesInventarios.objects.exclude(nombre = self.instance)
                abreviacion = abreviacion.get(abreviacion = form_data['abreviacion'])
                self._errors['abreviacion'] = ['El documento contable ya existe']
            except DocumentosContablesInventarios.DoesNotExist:
                pass 