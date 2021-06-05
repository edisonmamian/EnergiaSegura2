from django.urls import reverse
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
class CrearTipoIdentificacion (CreateView):
    model = TipoIdentificacion
    form_class = FormTipoIdentificacion
    template_name = 'comunes/tipoIdentificacion.html'

    def get_success_url(self):
        return reverse("comunes:crear_tipoIdentificacion")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = True
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CrearTipoIdentificacion, self).get_context_data(**kwargs)
        context['boton']= "Registrar"
        context['tipos']= TipoIdentificacion.objects.all()

        return context

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha registrado exitosamente el tipo de identificación"
        )
        return super(CrearTipoIdentificacion, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al registrar el tipo de identifiación, por favor revise los datos"
        )
        return super(CrearTipoIdentificacion, self).form_invalid(form)

class ActualizarTipoIdentificacion (UpdateView):
    model = TipoIdentificacion
    form_class = FormTipoIdentificacion
    template_name = 'comunes/tipoIdentificacion.html'

    def get_success_url(self):
        return reverse("comunes:crear_tipoIdentificacion")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = False
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(ActualizarTipoIdentificacion, self).get_context_data(**kwargs)
        context['boton']= "Actualizar"
        context['tipos']= TipoIdentificacion.objects.all()

        return context

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha actualizado exitosamente el tipo de identificación"
        )
        return super(ActualizarTipoIdentificacion, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al actualizar el tipo de identifiación, por favor revise los datos"
        )
        return super(ActualizarTipoIdentificacion, self).form_invalid(form)

########### CLASIFICACION DIAN
class CrearClasificacionDian (CreateView):
    model = ClasificacionDian
    form_class = FormClasificacionDian
    template_name = 'comunes/tipoIdentificacion.html'

    def get_success_url(self):
        return reverse("comunes:crear_clasificaciondian")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = True
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CrearClasificacionDian, self).get_context_data(**kwargs)
        context['boton']= "Registrar"
        context['tipos']= ClasificacionDian.objects.all()

        return context

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha registrado exitosamente la clasificación DIAN"
        )
        return super(CrearClasificacionDian, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al registrar la clasificación DIAN, por favor revise los datos"
        )
        return super(CrearClasificacionDian, self).form_invalid(form)

class ActualizarClasificacionDian (UpdateView):
    model = ClasificacionDian
    form_class = FormClasificacionDian
    template_name = 'comunes/clasificaciondian.html'

    def get_success_url(self):
        return reverse("comunes:crear_clasificaciondian")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = False
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(ActualizarClasificacionDian, self).get_context_data(**kwargs)
        context['boton']= "Actualizar"
        context['tipos']= ClasificacionDian.objects.all()

        return context

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha actualizado exitosamente la clasificación DIAN"
        )
        return super(ActualizarClasificacionDian, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al actualizar la clasificación DIAN, por favor revise los datos"
        )
        return super(ActualizarClasificacionDian, self).form_invalid(form)

########### TIPO CONTRIBUYENTE
class CrearTipoContribuyente (CreateView):
    model = TipoContribuyente
    form_class = FormTipoContribuyente
    template_name = 'comunes/tipocontribuyente.html'

    def get_success_url(self):
        return reverse("comunes:crear_tipocontribuyente")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = True
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CrearTipoContribuyente, self).get_context_data(**kwargs)
        context['boton']= "Registrar"
        context['tipos']= TipoContribuyente.objects.all()

        return context

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha registrado exitosamente el tipo de contribuyente"
        )
        return super(CrearTipoContribuyente, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al registrar el tipo de contribuyente, por favor revise los datos"
        )
        return super(CrearTipoContribuyente, self).form_invalid(form)

class ActualizarTipoContribuyente (UpdateView):
    model = TipoContribuyente
    form_class = FormTipoContribuyente
    template_name = 'comunes/tipocontribuyente.html'

    def get_success_url(self):
        return reverse("comunes:crear_tipocontribuyente")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = False
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(ActualizarTipoContribuyente, self).get_context_data(**kwargs)
        context['boton']= "Actualizar"
        context['tipos']= TipoContribuyente.objects.all()

        return context

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha actualizado exitosamente el tipo de contribuyente"
        )
        return super(ActualizarTipoContribuyente, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al actualizar el tipo de contribuyente, por favor revise los datos"
        )
        return super(ActualizarTipoContribuyente, self).form_invalid(form)

########### ACTIVIDAD ECONOMICA
class CrearActividadEconomica (CreateView):
    model = ActividadEconomica
    form_class = FormActividadEconomica
    template_name = 'comunes/actividadeconomica.html'

    def get_success_url(self):
        return reverse("comunes:crear_actividadeconomica")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = True
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CrearActividadEconomica, self).get_context_data(**kwargs)
        context['boton']= "Registrar"
        context['tipos']= ActividadEconomica.objects.all()

        return context

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha registrado exitosamente la actividad económica"
        )
        return super(CrearActividadEconomica, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al registrar la actividad económica, por favor revise los datos"
        )
        return super(CrearActividadEconomica, self).form_invalid(form)

class ActualizarActividadEconomica (UpdateView):
    model = ActividadEconomica
    form_class = FormActividadEconomica
    template_name = 'comunes/actividadeconomica.html'

    def get_success_url(self):
        return reverse("comunes:crear_actividadeconomica")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = False
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(ActualizarActividadEconomica, self).get_context_data(**kwargs)
        context['boton']= "Actualizar"
        context['tipos']= ActividadEconomica.objects.all()

        return context

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha actualizado exitosamente la actividad económica"
        )
        return super(ActualizarActividadEconomica, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al actualizar la actividad económica, por favor revise los datos"
        )
        return super(ActualizarActividadEconomica, self).form_invalid(form)

########### RESPONSABILIDADES
class CrearTiposResponsabilidades (CreateView):
    model = TiposResponsabilidades
    form_class = FormTiposResponsabilidades
    template_name = 'comunes/responsabilidadfiscal.html'

    def get_success_url(self):
        return reverse("comunes:crear_responsabilidadfiscal")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = True
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CrearTiposResponsabilidades, self).get_context_data(**kwargs)
        context['boton']= "Registrar"
        context['tipos']= TiposResponsabilidades.objects.all()

        return context

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha registrado exitosamente la responsabilidad fiscal"
        )
        return super(CrearTiposResponsabilidades, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al registrar la responsabilidad fiscal, por favor revise los datos"
        )
        return super(CrearTiposResponsabilidades, self).form_invalid(form)

class ActualizarTiposResponsabilidades (UpdateView):
    model = TiposResponsabilidades
    form_class = FormTiposResponsabilidades
    template_name = 'comunes/responsabilidadfiscal.html'

    def get_success_url(self):
        return reverse("comunes:crear_responsabilidadfiscal")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = False
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(ActualizarTiposResponsabilidades, self).get_context_data(**kwargs)
        context['boton']= "Actualizar"
        context['tipos']= TiposResponsabilidades.objects.all()

        return context

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha actualizado exitosamente la responsabilidad fiscal"
        )
        return super(ActualizarTiposResponsabilidades, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al actualizar la responsabilidad fiscal, por favor revise los datos"
        )
        return super(ActualizarTiposResponsabilidades, self).form_invalid(form)