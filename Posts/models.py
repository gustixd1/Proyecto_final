from django.db import models
from django.conf import settings

# Create your models here.
class Publicaciones(models.Model):
    titulo = models.CharField(max_length=50)
    bajada = models.CharField(max_length=300)
    fecha = models.DateField(max_length=30, help_text = "Por favor, ingrese la fecha en el formato DD/MM/YYYY.")
    cuerpo = models.CharField(max_length=3000)
    imagen = models.ImageField(upload_to="foto_publicacion", null=True, blank=True)
    
    def __str__(self):
        return f"{settings.MEDIA_URL}{self.imagen}"
