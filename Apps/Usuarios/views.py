from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, FormView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.http import HttpResponseRedirect, HttpResponse
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
    
class CrearUsuario (CreateView):
    model = Usuario
    form_class = FormUsuario
    template_name = 'Usuarios/usuarios.html'

    def get_success_url(self):
        return reverse("usuarios:usuarios_crear")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = True
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(CrearUsuario, self).get_context_data(**kwargs)
        context['boton']= "Registrar"
        context['tipos']= Usuario.objects.all()
        return context

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha actualizado exitosamente el usuario"
        )
        return super(CrearUsuario, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al actualizar el usuario, por favor revise los datos"
        )
        return super(CrearUsuario, self).form_invalid(form)

class EditarUsuario (UpdateView):
    model = Usuario
    form_class = FormUsuario
    template_name = 'Usuarios/usuarios.html'

    def get_success_url(self):
        return reverse("usuarios:usuarios_crear")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['crear'] = False
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(EditarUsuario, self).get_context_data(**kwargs)
        context['boton']= "Actualizar"
        context['tipos']= Usuario.objects.all()
        return context

    def form_valid (self, form):
        messages.success (
            self.request,
            "Se ha actualizado exitosamente el usuario"
        )
        return super(EditarUsuario, self).form_valid(form)

    def form_invalid (self, form):
        messages.error (
            self.request,
            "Error al actualizar el usuario, por favor revise los datos"
        )
        return super(EditarUsuario, self).form_invalid(form)

class LoginUsuario(FormView):
    template_name = 'usuarios/login.html'
    form_class = LoginForm
    success_url = reverse_lazy ('Usuarios:listar')

    def form_valid(self, form):
        credentials = form.cleaned_data

        user = authenticate(
            username = credentials['username'],
            password = credentials['password']
        )

        if user is not None:
            login (self.request, user)
            return HttpResponseRedirect(self.success_url)
        else:
            messages.error(
                self.request,
                "No se pudo autenticar en el sistema"
            )
            return HttpResponseRedirect(reverse_lazy('usuarios:login'))

def LogoutUsuario(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('usuarios:login'))