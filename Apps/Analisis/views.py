from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
class CrearFase (CreateView):
    model = Fases
    form_class = FormFases
    template_name = 'Anaslisis/fases.html'

    def get_success_url(self):
        return reverse("Analisis:crear_fase")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = True
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CrearFase, self).get_context_data(**kwargs)
        context['boton']= "Registrar"
        context['tipos']= Fases.objects.all()

        return context

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha registrado exitosamente la fase"
        )
        return super(CrearFase, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al registrar la fase, por favor revise los datos"
        )
        return super(CrearFase, self).form_invalid(form)

class ActualizarFase (UpdateView):
    model = Fases
    form_class = FormFases
    template_name = 'Anaslisis/fases.html'

    def get_success_url(self):
        return reverse("Analisis:crear_fase")

    def dispatch(self, request, *args, **kwargs):
        try:
            Fases.objects.get(id = self.kwargs['pk'])
        except Fases.DoesNotExist:
            messages.error (
                self.request,
                "El tipo de objeto de ensayo al que intenta acceder no existe"
            )
            return redirect("ObjEnsayo:crear")        
        return super(ActualizarFase, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = False
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(ActualizarFase, self).get_context_data(**kwargs)
        context['boton']= "Actualizar"
        context['tipos']= Fases.objects.all()

        return context

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha actualizado exitosamente la fase"
        )
        return super(ActualizarFase, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al actualizar la fase, por favor revise los datos"
        )
        return super(ActualizarFase, self).form_invalid(form)

################## Analisis 

class CrearAnalisis (CreateView):
    model = Analisis
    form_class = FormAnalisis
    template_name = 'Anaslisis/analisis.html'

    def get_success_url(self):
        return reverse("Analisis:crear_fase")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = True
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CrearAnalisis, self).get_context_data(**kwargs)
        context['boton']= "Registrar"
        context['tipos']= Analisis.objects.all()

        return context

class ActualizarAnalisis (UpdateView):
    model = Analisis
    form_class = FormAnalisis
    template_name = 'Anaslisis/analisis.html'

    def get_success_url(self):
        return reverse("Analisis:crear_fase")

    def dispatch(self, request, *args, **kwargs):
        try:
            Analisis.objects.get(id = self.kwargs['pk'])
        except Analisis.DoesNotExist:
            messages.error (
                self.request,
                "El análisis al que intenta acceder no existe"
            )
            return redirect("ObjEnsayo:crear")        
        return super(ActualizarAnalisis, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = True
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(ActualizarAnalisis, self).get_context_data(**kwargs)
        context['boton']= "Registrar"
        context['tipos']= Analisis.objects.all()

        return context