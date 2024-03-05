from django.urls import path
from Home.views import *

urlpatterns = [
    path("", VistaInicio.as_view()),
    path("inicio/", VistaInicio.as_view(), name="Inicio"),
    path("sobreMi/", sobreMi, name="Sobre Mi"),
]