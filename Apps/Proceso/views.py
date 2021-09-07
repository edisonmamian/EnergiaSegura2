from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib import messages
from django.db.models import Q
from .models import *
from .forms import *

from Apps.Recepcion.models import Recepcion, ItemRecibido

# Create your views here.
class Proceso (CreateView):
   model = Proceso 
   form_class = FormProceso
   template_name = 'Proceso/registrar.html'

   def dispatch(self, *args, **kwargs):
        try:
            ItemRecibido.objects.get(id = self.kwargs['pk'])
        except ItemRecibido.DoesNotExist:
            messages.warning(self.request, "La recepción a la que esta intentando acceder no existe")
            return redirect('Proceso:items')
        return super(Proceso, self).dispatch(*args, **kwargs)

   def get_context_data(self, **kwargs):
        context = super(Proceso, self).get_context_data(**kwargs)		
        
        itemRecibido = ItemRecibido.objects.get(id=self.kwargs['pk'])
        analisis = itemRecibido.item.all()
		
        context['itemRecibido'] = itemRecibido
        context['numero_criterios'] = analisis
        return context

class ListarRecepciones (ListView):
    model = Recepcion
    template_name = "Proceso/listar_recepcion.html"

    def get_queryset(self):		
        queryset = Recepcion.objects.filter(Q(estadoProceo=1) | Q(estadoProceo = 2))
        return queryset

class ListarCilindros (ListView):
    model = Recepcion
    template_name = "Proceso/listar_cilindros.html"

    def dispatch(self, *args, **kwargs):
        try:
            Recepcion.objects.get(id = self.kwargs['pk'])
        except Recepcion.DoesNotExist:
            messages.warning(self.request, "La recepción a la que esta intentando acceder no existe")
            return redirect('Proceso:recepciones')
        return super(ListarCilindros, self).dispatch(*args, **kwargs)

    def get_queryset(self):		
        queryset = ItemRecibido.objects.filter(recepcion=self.self.kwargs['pk'])
        return queryset