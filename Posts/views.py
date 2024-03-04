from django.shortcuts import render
from Posts.models import Publicaciones

# Clases basadas en vistas
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class ListaPublicaciones(ListView):
    model = Publicaciones
    template_name = "Posts/post_list.html"
    context_object_name = "objects"

class DetallePublicaciones(DetailView):
    model = Publicaciones
    template_name = "Posts/post_detalle.html"
    context_object_name = "objects"

class CreacionPublicaciones(CreateView):
    model = Publicaciones
    success_url = "Nuevo"
    fields = ["titulo", "bajada", "fecha", "cuerpo"]
    template_name = "Posts/post-formulario"

class EliminarPublicacion(DeleteView):
    model = Publicaciones
    success_url = "Publicaciones"
    template_name = "Posts/post-eliminar.html"
