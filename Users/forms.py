from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(label="Usuario", min_length=5, max_length=30)
    password1 = forms.CharField(label="Ingrese su contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita su contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.CharField(label="Modificar correo", min_length=5, max_length=30)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita su contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField(label="Nombre")
    first_name = forms.CharField(label="Apellido")
    
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]
        help_texts = {k:"" for k in fields}