from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.
class CrearObjEnsayo (CreateView):
    model = TiposObjEnsayo
    form_class = FormTiposObjEnsayo
    template_name = 'ObjEnsayo/formulario.html'

    def get_success_url(self):
        return reverse("ObjEnsayo:crear")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = True
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CrearObjEnsayo, self).get_context_data(**kwargs)
        context['boton']= "Registrar"
        context['tipos']= TiposObjEnsayo.objects.all()

        return context

class ActualizarObjEnsayo (UpdateView):
    model = TiposObjEnsayo
    form_class = FormTiposObjEnsayo
    template_name = 'ObjEnsayo/formulario.html'

    def get_success_url(self):
        return reverse("ObjEnsayo:crear")

    def dispatch(self, request, *args, **kwargs):
        #print (self)
        try:
            TiposObjEnsayo.objects.get(id = self.kwargs['pk'])
        except TiposObjEnsayo.DoesNotExist:
            messages.error (
                self.request,
                "El tipo de objeto de ensayo al que intenta acceder no existe"
            )
            return redirect("ObjEnsayo:crear")        
        return super(ActualizarObjEnsayo, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ActualizarObjEnsayo, self).get_context_data(**kwargs)
        context['boton']= "Actualizar"
        context['tipos']= TiposObjEnsayo.objects.all()

        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = False
        return kwargs