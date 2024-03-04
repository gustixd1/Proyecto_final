from django.shortcuts import render
from Users.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    
    if request.method == "POST":
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "Users/login.html", {"mensaje":"Usuario creado exitosamente"})
    
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
                
                return render(request, "Home/index.html", {"mensaje" : f"Bienvenido {usuario}"})
            else:
                form = AuthenticationForm()
                return render(request, "Users/login.html", {"mensaje" : "Error, datos incorrectos", "form":form})
        
        else:
            form = AuthenticationForm()
            return render(request, "Users/login.html", {"mensaje" : "Error, formulario erróneo", "form":form})
    else:
        form = AuthenticationForm()
        return render(request, "Users/login.html", {"form":form})

@login_required
def edit_user(request):

    usuario = request.user

    if request.method == 'POST':

        form = UserEditForm(request.POST)

        if form.is_valid():

            informacion = form.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "Home/index.html")

    else:

        form = UserEditForm(initial={'email': usuario.email})

    return render(request, "Users/edit_user.html", {"form": form, "usuario": usuario})

