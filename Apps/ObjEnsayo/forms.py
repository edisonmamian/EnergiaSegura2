from django import forms

from .models import *

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
        print ("clean")
        print (self.crear)
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
