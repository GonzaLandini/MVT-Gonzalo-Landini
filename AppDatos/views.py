from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Datos_de_familia

# Create your views here.

def funcion_datos_familia(request):

    familiar1=Datos_de_familia(nombre="Gonzalo", edad=27, anio_nacimiento="1995-01-19", email="gonzalo@landini.com")
    familiar2=Datos_de_familia(nombre="Padre", edad=62, anio_nacimiento="1960-12-24", email="padre@landini.com")
    familiar3=Datos_de_familia(nombre="Madre", edad=65, anio_nacimiento="1957-08-13", email="madre@landini.com")
    familiar4=Datos_de_familia(nombre="Hermano", edad=30, anio_nacimiento="1992-05-16", email="hermano@landini.com")
    familiar1.save()
    familiar2.save()
    familiar3.save()
    familiar4.save()

    diccionario={"familiar1":familiar1, "familiar2":familiar2,"familiar3":familiar3, "familiar4":familiar4}
    plantilla=loader.get_template("template1.html")
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)