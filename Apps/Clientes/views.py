from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
class CrearClasificacion (CreateView):
    model = ClasificacionClientes
    form_class = FormClasificacion
    template_name = 'Clientes/clasificacion.html'

    def get_success_url(self):
        return reverse("Clientes:crear_clasificacion")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = True
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CrearClasificacion, self).get_context_data(**kwargs)
        context['boton']= "Registrar"
        context['tipos']= ClasificacionClientes.objects.all()

        return context

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha registrado exitosamente la clasificación"
        )
        return super(CrearClasificacion, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al registrar la clasificación, por favor revise los datos"
        )
        return super(CrearClasificacion, self).form_invalid(form)

class ActualizarClasificacion (CreateView):
    model = ClasificacionClientes
    form_class = FormClasificacion
    template_name = 'Clientes/clasificacion.html'

    def get_success_url(self):
        return reverse("Clientes:crear_clasificacion")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = False
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(ActualizarClasificacion, self).get_context_data(**kwargs)
        context['boton']= "Registrar"
        context['tipos']= ClasificacionClientes.objects.all()

        return context

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha actualizado exitosamente la clasificación"
        )
        return super(ActualizarClasificacion, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al actualizar la clasificación, por favor revise los datos"
        )
        return super(ActualizarClasificacion, self).form_invalid(form)