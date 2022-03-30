from django.shortcuts import render
from django.http import HttpResponse
from models import Curso

def Curso(self):

    curso = Curso(nombre='Web', camada='1111')

    curso.save()

    documento = f'el curso es: {curso.nombre}, la camada: {curso.camada}'

    return HttpResponse(documento)

# Create your views here.
