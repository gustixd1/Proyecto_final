from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from Users.forms import UserRegisterForm, UserEditForm
from Users.models import Avatar

# Create your views here.
def register(request):
    
    if request.method == "POST":
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            user = form.save()
            redireccion = request.GET.get("next", "/")
            login(request, user)
            return redirect(redireccion)
            # return render(request, "Users/login.html", {"mensaje":"Usuario creado exitosamente"})
    
    else:
        
        form = UserRegisterForm()
        
    return render(request, "Users/registro.html", {"form":form})

def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contrasena = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password = contrasena)
            
            if user is not None:
                login(request, user)
                
                redireccion = request.GET.get("next", "/")
                return redirect(redireccion)
        
        else:
            form = AuthenticationForm()
            return render(request, "Users/login.html", {"mensaje" : "Datos incorrectos", "form":form})
    else:
        form = AuthenticationForm()
        return render(request, "Users/login.html", {"form":form})


@login_required
def edit_user(request):

    usuario = request.user

    if request.method == 'POST':

        form = UserEditForm(request.POST, request.FILES)

        if form.is_valid():

            informacion = form.cleaned_data

            if informacion["password1"] != informacion["password2"]:
                datos = {
                    'first_name': usuario.first_name,
                    'email': usuario.email
                }
                form = UserEditForm(initial=datos)

            else:
                usuario.email = informacion['email']
                if informacion["password1"]:
                    usuario.set_password(informacion["password1"])
                usuario.last_name = informacion['last_name']
                usuario.first_name = informacion['first_name']
                usuario.save()

                try:
                    avatar = Avatar.objects.get(user=usuario)
                except Avatar.DoesNotExist:
                    avatar = Avatar(user=usuario, imagen=informacion["imagen"])
                    avatar.save()
                else:
                    avatar.imagen = informacion["imagen"]
                    avatar.save()

                return redirect(request.GET.get("next", "/"))

    else:
        datos = {
            'first_name': usuario.first_name,
            'email': usuario.email
        }
        form = UserEditForm(initial=datos)

    return render(request, "Users/editar-usuario.html", {"form": form, "usuario": usuario})