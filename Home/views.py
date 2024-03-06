from typing import Any
from django.shortcuts import render
from Posts.models import Publicaciones
from Users.models import Avatar
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    publicaciones = Publicaciones.objects.order_by('-fecha')[:2]
    return render(request, "Home/index.html", {"publicaciones" : publicaciones})
    
def sobreMi(request):
    return render(request, "Home/about.html")
