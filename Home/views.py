from django.shortcuts import render
from django.views.generic import ListView
from Posts.models import Publicaciones
from Users.models import Avatar

# Create your views here.

def sobreMi(request):
    return render(request, "Home/about.html")

class VistaInicio(ListView):
    template_name = "Home/index.html"
    context_object_name = "objects"
    
    def get_queryset(self):
        return Publicaciones.objects.order_by('-fecha')[:2]