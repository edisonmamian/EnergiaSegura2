from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView
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

class ActualizarClasificacion (UpdateView):
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

######################## CLIENTES 

class CrearClientes (CreateView):
    model = Clientes
    form_class = FormCliente
    template_name = 'Clientes/clientes.html'

    def get_success_url(self):
        return reverse("Clientes:crear_clasificacion")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = True
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CrearClientes, self).get_context_data(**kwargs)
        context['boton']= "Registrar"

        return context

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha registrado exitosamente el cliente"
        )
        return super(CrearClientes, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al registrar el cliente, por favor revise los datos"
        )
        return super(CrearClientes, self).form_invalid(form)

class ActualizarClientes (UpdateView):
    model = Clientes
    form_class = FormCliente
    template_name = 'Clientes/clientes.html'

    def get_success_url(self):
        return reverse("Clientes:crear_clasificacion")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = False
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(ActualizarClientes, self).get_context_data(**kwargs)
        context['boton']= "Registrar"

        return context

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha actualizado exitosamente el cliente"
        )
        return super(ActualizarClientes, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al actualizar el cliente, por favor revise los datos"
        )
        return super(ActualizarClientes, self).form_invalid(form)

class ListarClients (ListView):
    model = Clientes
    template_name = 'Clientes/listarClientes.html'