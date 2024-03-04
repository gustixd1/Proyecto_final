from django.urls import path
from Posts.views import *

urlpatterns = [
    path("publicaciones/", ListaPublicaciones.as_view(), name="Publicaciones"),
    path("detalle-publicacion/", DetallePublicaciones.as_view(), name="Detalles"),
    path("crear-publicacion/", CreacionPublicaciones.as_view(), name="Nuevo"),
    path("eliminar-publicacion/", EliminarPublicacion.as_view(), name="Eliminar"),
]