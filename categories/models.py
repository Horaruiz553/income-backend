from django.db import models

# Create your models here.
class Categorie (models.Model):
    descripcion = models.CharField(max_length=100)
    ingreso = models.BooleanField(default=False)
