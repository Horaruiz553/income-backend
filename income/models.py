from django.db import models

# Create your models here.
from categories.models import Categorie
from users.models import User


class Income (models.Model):
    idusuario = models.ForeignKey(User, on_delete=models.CASCADE,)
    idcategoria = models.ForeignKey(Categorie, on_delete=models.CASCADE,)
    fecha = models.DateField(max_length=100)
    descripcion = models.CharField(max_length=100)
    monto = models.IntegerField()

    def __unicode__(self):
        return self.name

    @property
    def user_name(self):
        return self.idusuario.nombre
