from django import forms

class FormularioPublicacion(forms.Form):
    titulo = forms.CharField(max_length=50)
    bajada = forms.CharField(max_length=30)
    fecha = forms.CharField(max_length=30)
    cuerpo = forms.CharField(max_length=3000)    