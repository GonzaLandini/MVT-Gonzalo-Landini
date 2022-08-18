from django.db import models


# Create your models here.

class Datos_de_familia(models.Model):
    nombre= models.CharField(max_length=50)
    edad=models.IntegerField()
    anio_nacimiento=models.DateField()
    email=models.EmailField()