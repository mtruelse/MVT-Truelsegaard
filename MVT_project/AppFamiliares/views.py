from django.shortcuts import render
from AppFamiliares.models import Familiar

# Create your views here.

def familiares(request):
    mama = Familiar(nombre="Juana", edad="50", fecha_nacimiento="1972-03-25")
    mama.save()

    papa = Familiar(nombre="Jorge", edad="60", fecha_nacimiento="1962-05-26")
    papa.save()

    hermano = Familiar(nombre="Roberto", edad="35", fecha_nacimiento="1987-02-19")
    hermano.save()

    return render(request, 'template_1.html', {"nombre_madre": mama.nombre, "edad_madre": mama.edad, "nacimiento_madre": mama.fecha_nacimiento, "nombre_padre": papa.nombre, "edad_padre": papa.edad, "nacimiento_padre": papa.fecha_nacimiento, "nombre_hermano": hermano.nombre, "edad_hermano": hermano.edad, "nacimiento_hermano": hermano.fecha_nacimiento})


