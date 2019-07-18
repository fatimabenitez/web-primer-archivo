from django.shortcuts import render
from django.http import HttpResponse
from pendientes.models import Tarea 
from random import randint

# Create your views here.

def index(request):
    # saludo = "Hola, Fatima! Esta es la raiz /"
    listita= Tarea.objects.all()

    persona ={
    "nombre": "Fatima",
    "edad":34,
    "hobbies":["Cocinar","Leer","bailar"],
    "lista_tareas": listita, 
        }
    return render(request,"inicio.html",persona)

def vista_tarea(request):
    vista = "<h1> Hola, Mundo! Esta es la raiz </h1>"
    return HttpResponse(vista)

def vista_respuesta(request):
    vista = "<h1> Hola, Mundo! Esta es la raiz </h1>"
    return HttpResponse(vista)

def aleatorio (request):
    numero=str(randint(100,999))
    respuesta= "El numero ganador es: " + numero
    return HttpResponse(respuesta)
    

# 1- crear la vista/funcion tarea y conectar con la direccion
# /tareas en el archivo urls.py
# despues ir al navegdor y abrir htpp:....../tareas
#2.crear una vista respuestas que retorne un texto cuando
# en el navegador entemos al http:......./info
# pista crear una funcion/vista en views.py y conectar en
# urls.py usando path (.....) 