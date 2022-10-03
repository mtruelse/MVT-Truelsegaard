from django.shortcuts import render
from AppFamiliares.models import Familiar

# Create your views here.

def familiares(request):
    mama = Familiar(nombre="Marisa", edad="57", fecha_nacimiento="1965-01-25")
    mama.save()
    return render(request, 'template_1.html', {"nombre": mama.nombre, "edad": mama.edad, "nacimiento": mama.fecha_nacimiento})