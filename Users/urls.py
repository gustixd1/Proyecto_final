from django.urls import path
from Users.views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("registro/", register, name="Registro"),
    path("login/", login_request, name="Login"),
    path("logout/", LogoutView.as_view(template_name="Home/index.html"), name = "Logout"),
    path("editar_perfil", edit_user, name="Editar perfil")
]