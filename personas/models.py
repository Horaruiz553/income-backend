from django.db import models

# Create your models here.
class Persona (models.Model):
    name = models.CharField(max_length=100)
    lastname = models.URLField(max_length=100)
    email = models.URLField(max_length=100)