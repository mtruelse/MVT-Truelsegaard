from django.shortcuts import render
from AppFamiliares.models import Familiar

# Create your views here.

def familiares(request):
    mama = Familiar(nombre="Marisa", edad="57", fecha_nacimiento="1965-01-25")
    mama.save()

    papa = Familiar(nombre="José", edad="63", fecha_nacimiento="1959-06-28")
    papa.save()

    hermano = Familiar(nombre="Martín", edad="32", fecha_nacimiento="1990-01-19")
    hermano.save()

    return render(request, 'template_1.html', {"nombre_madre": mama.nombre, "edad_madre": mama.edad, "nacimiento_madre": mama.fecha_nacimiento, "nombre_padre": papa.nombre, "edad_padre": papa.edad, "nacimiento_padre": papa.fecha_nacimiento, "nombre_hermano": hermano.nombre, "edad_hermano": hermano.edad, "nacimiento_hermano": hermano.fecha_nacimiento})


