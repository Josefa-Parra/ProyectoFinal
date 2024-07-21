from django.shortcuts import render
from .models import *

def home(request):
    return render(request,'AppViajes/index.html')

def proposito(request):
    return render(request,'AppViajes/proposito.html')

def registrarse(request):
    contexto = {"registrarse": Registrarse.objects.all()}
    return render(request,'AppViajes/registrarse.html',contexto)

def crear_viaje(request):
    contexto = {"registrarse": Crear_Viaje.objects.all()}
    return render(request,'AppViajes/crear_viaje.html',contexto)

def participar(request):
    contexto = {"registrarse": Participar.objects.all()}
    return render(request,'AppViajes/participar.html',contexto)