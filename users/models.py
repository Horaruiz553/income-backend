from django.db import models

# Create your models here.
class User (models.Model):
    usuario = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
