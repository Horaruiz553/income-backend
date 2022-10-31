from django.db import models

from categories.models import Categorie
from users.models import User


class Egress (models.Model):
    idusuario = models.ForeignKey(User, on_delete=models.CASCADE,)
    idcategoria = models.ForeignKey(Categorie, on_delete=models.CASCADE,)
    fecha = models.DateField(max_length=100)
    descripcion = models.CharField(max_length=100)
    monto = models.IntegerField()
