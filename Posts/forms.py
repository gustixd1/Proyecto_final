from django import forms
from Posts.models import Publicaciones

class FormularioPublicacion(forms.Form):
    titulo = forms.CharField(max_length=50)
    bajada = forms.CharField(max_length=300)
    autor = forms.CharField(max_length=50)
    fecha = forms.DateField(max_length=30)
    cuerpo = forms.CharField(max_length=3000)
    imagen = forms.ImageField()
    
    class Meta:
        model = Publicaciones
        fields = ['fecha']
        input_formats = ["%d/%m/%y"]
        widgets = {
            'fecha': forms.DateInput(attrs={'placeholder': 'DD/MM/YYYY', 'pattern': '\d{2}/\d{2}/\d{4}'}),
        }
        help_text = {k:"" for k in fields}

    