from django.shortcuts import render
from .models import Usuarios
from .forms import UsuariosForm
from django.views.generic import CreateView,DetailView, ListView, UpdateView,DeleteView
from django.core.urlresolvers import reverse


# Create your views here.

class ListaUsuarios(ListView):
    model = Usuarios
    template_name = "lista.html"

class CrearUsuario(CreateView):
    model = Usuarios
    form_class = UsuariosForm
    template_name = "crear.html"

    def get_success_url(self):
        return reverse('usuarios:index')

class VerUsario(DetailView):
    pk_url_kwarg ='usuarios_id'
    model = Usuarios
    template_name = "ver.html"

class ModificarUsuario(UpdateView):
    model = Usuarios
    form_class = UsuariosForm
    template_name = "crear.html"

    def get_success_url(self):
        return reverse('usuarios:index')


class BorrarUsuario(DeleteView):
    model = Usuarios
    template_name = ""