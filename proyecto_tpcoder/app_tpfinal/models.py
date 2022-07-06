from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Productos(models.Model):

    nombre_prod = models.CharField(max_length=100)
    codigo_prod = models.IntegerField()
    precio_prod = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre_prod} - Codigo:{self.codigo_prod} - Precio:{self.precio_prod}"

class Clientes(models.Model):
    nombre = models.CharField(max_length=80)
    obra_social = models.CharField(max_length=100)
    codigo_os = models.IntegerField()
    nacimiento = models.DateField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Obra social: {self.obra_social} - Fecha nacimiento: {self.nacimiento}"

class Obra_social(models.Model):
    nombre = models.CharField(max_length=80)
    codigo_os = models.IntegerField()
    nombre_prod = models.CharField(max_length=80)
    codigo_prod = models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Codigo os: {self.codigo_os} - Codigo prod: {self.codigo_prod}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares' , null=True , blank=True) 



    