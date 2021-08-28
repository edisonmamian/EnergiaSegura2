from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
class CrearRecepcion (CreateView):
    model = Recepcion
    form_class = FormRecepcion
    template_name = 'Recepcion/recepcion.html'

    def get_success_url(self):
        return reverse("Recepcion:crear")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = True
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CrearRecepcion, self).get_context_data(**kwargs)
        context['boton']= "Registrar"

        if self.request.POST:
            context['itemRecibido'] = Formset_Recepcion_ItemRecibido (
                self.request.POST
            )
        else:
            context['itemRecibido'] = Formset_Recepcion_ItemRecibido ()
        
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        itemRecibido = context['itemRecibido']

        if itemRecibido.is_valid():
            self.object = form.save()
            itemRecibido.instance = self.object
            itemRecibido.save()
        else:
            messages.error (
                self.request,
                "Error al realizar la recepción, por favor revise los datos"
            )
            return super(CrearRecepcion, self).form_invalid(form)
        messages.success(
            self.request,
            "Se ha registrado exitosamente la recepción"
        )
        return super(CrearRecepcion, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Error al realizar la recepción, por favor revise los datos"
        )
        return super(CrearRecepcion, self).form_invalid(form)

class ActualizarRecepcion (UpdateView):
    model = Recepcion
    form_class = FormRecepcion
    template_name = 'Recepcion/recepcion.html'

    def get_success_url(self):
        return reverse("Recepcion:crear")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = False
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        try:
            Recepcion.objects.get(id = self.kwargs['pk'])
        except Recepcion.DoesNotExist:
            messages.error (
                self.request,
                "El tipo de objeto de ensayo al que intenta acceder no existe"
            )
            return redirect("ObjEnsayo:crear")        
        return super(ActualizarRecepcion, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ActualizarRecepcion, self).get_context_data(**kwargs)
        context['boton']= "Actualizar"

        if self.request.POST:
            context['itemRecibido'] = Formset_Recepcion_ItemRecibido (
                self.request.POST,
                instance=self.object
            )
        else:
            context['itemRecibido'] = Formset_Recepcion_ItemRecibido (
                instance=self.object
            )

        return context

class ListarRecepcion (ListView):
    model = Recepcion