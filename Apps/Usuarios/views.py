from django.urls import reverse
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
class CrearRoles (CreateView):
    model = Roles
    form_class = FormGrupos
    template_name = 'Usuarios/grupos.html'

    def get_success_url(self):
        return reverse("usuarios:roles_crear")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = True
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CrearRoles, self).get_context_data(**kwargs)
        context['boton']= "Registrar"
        context['tipos']= Roles.objects.all()
        return context

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha registrado exitosamente el rol"
        )
        return super(CrearRoles, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al registrar el rol, por favor revise los datos"
        )
        return super(CrearRoles, self).form_invalid(form)

class EditarRoles (UpdateView):
    model = Roles
    form_class = FormGrupos
    template_name = 'Usuarios/grupos.html'

    def get_success_url(self):
        return reverse("usuarios:roles_crear")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = False
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(EditarRoles, self).get_context_data(**kwargs)
        context['boton']= "Actualizar"
        context['tipos']= Roles.objects.all()
        return context

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha actualizado exitosamente el rol"
        )
        return super(EditarRoles, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al actualizar el rol, por favor revise los datos"
        )
        return super(EditarRoles, self).form_invalid(form)
    
