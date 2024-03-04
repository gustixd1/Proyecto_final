from django.db import models

# Create your models here.
class Publicaciones(models.Model):
    titulo = models.CharField(max_length=50)
    bajada = models.CharField(max_length=300)
    fecha = models.CharField(max_length=30)
    cuerpo = models.CharField(max_length=3000)
