from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(User):
    class Meta:
        proxy = True


class Nucleos(models.Model):
    nombre = models.CharField(max_length=20, null=False)
    integrantes = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre 

class Integrantes(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class DatosPersonales(models.Model):
    nombre = models.CharField(verbose_name='Nombre y apellidos', max_length=100)
    carnet_ident = models.PositiveIntegerField(default=0)
    trabaja = models.BooleanField(verbose_name='Trabaja', default=False)
    estudia = models.BooleanField(verbose_name='Estudia', default=False)
    desocupado = models.BooleanField(verbose_name='Desocupado', default=False)
    centro = models.CharField(verbose_name='Centro de estudio o trabajo', max_length=100, blank=True, null=True)
    user = models.ForeignKey(Integrantes, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre