from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView
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

        if self.request.POST:
            context['analisis'] = FormSet_ObjEnsayo_Analisis (
                self.request.POST
            )
        else:
            context['analisis'] = FormSet_ObjEnsayo_Analisis ()

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        analisis = context['analisis']

        if analisis.is_valid():
            self.object = form.save()
            analisis.instance = self.object
            analisis.save()
        else:
            messages.error (
                self.request,
                "Error al registrar el objeto de ensayo, por favor revise los datos"
            )
            return super(CrearObjEnsayo, self).form_invalid(form)
        messages.success(
            self.request,
            "Se ha registrado exitosamente el objeto de ensayo"
        )
        return super(CrearObjEnsayo, self).form_valid(form)
    
    def form_invalid(self, form):
        messages.error(
            self.request,
            "Error al registrar el objeto de ensayo, por favor revise los datos"
        )
        return super(CrearObjEnsayo, self).form_invalid(form)

class ActualizarObjEnsayo (UpdateView):
    model = TiposObjEnsayo
    form_class = FormTiposObjEnsayo
    template_name = 'ObjEnsayo/formulario.html'

    def get_success_url(self):
        return reverse("ObjEnsayo:crear")

    def dispatch(self, request, *args, **kwargs):
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

        if self.request.POST:
            context['analisis'] = FormSet_ObjEnsayo_Analisis (
                self.request.POST,
                instance=self.object
            )
        else:
            context['analisis'] = FormSet_ObjEnsayo_Analisis (
                instance=self.object
            )

        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = False
        return kwargs

    def form_valid (self, form):
        context = self.get_context_data()
        analisis = context ['analisis']

        if analisis.is_valid():
            self.object = form.save()
            analisis.instance = self.object
            analisis.save()
        else:
            messages.error (
                self.request,
                "Error al actualizar el objeto de ensayo, por favor revise los datos"
            )
            return super(ActualizarObjEnsayo, self).form_invalid(form)

        messages.success (
            self.request,
            "Se ha actualizado exitosamente el objeto de ensayo"
        )
        return super(ActualizarObjEnsayo, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al actualizar el objeto de ensayo, por favor revise los datos"
        )
        return super(ActualizarObjEnsayo, self).form_invalid(form)