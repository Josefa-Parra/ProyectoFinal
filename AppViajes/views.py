from django.shortcuts import render
from .models import *
from .forms import *

def home(request):
    return render(request,'AppViajes/index.html')

def proposito(request):
    return render(request,'AppViajes/proposito.html')

def registrarse(request):
    contexto = {"registrarse": Registrarse.objects.all()}
    return render(request,'AppViajes/registrarse.html',contexto)

def crear_viaje(request):
    contexto = {"crear_viaje": Crear_Viaje.objects.all()}
    return render(request,'AppViajes/crear_viaje.html',contexto)

def participar(request):
    contexto = {"participar": Participar.objects.all()}
    return render(request,'AppViajes/participar.html',contexto)
#formularios
def registrarse_Form(request):
    if request.method == "POST":
        miForm = registrarseForm(request.POST)
        if miForm.is_valid():
            registrarse_nombre= miForm.cleaned_data.get("nombre")
            registrarse_apellido= miForm.cleaned_data.get("apellido")
            registrarse_email= miForm.cleaned_data.get("email")
            registrarse_ciudad= miForm.cleaned_data.get("ciudad")
            registrarse = Registrarse(nombre=registrarse_nombre, 
                                      apellido=registrarse_apellido, 
                                      email=registrarse_email, 
                                      ciudad=registrarse_ciudad)
            registrarse.save()
            contexto = {"registrarse": Registrarse.objects.all()}
            return render(request,'AppViajes/registrarse.html', contexto)
    else:
        miForm = registrarseForm()
    
    return render(request, "AppViajes/registrarseForm.html", {"form": miForm})

def crear_viaje_Form(request):
    if request.method == "POST":
        miForm = crear_viajeForm(request.POST)
        if miForm.is_valid():
            crear_viaje_nombre_tutor= miForm.cleaned_data.get("nombre_tutor")
            crear_viaje_lugar= miForm.cleaned_data.get("lugar")
            crear_viaje_dia= miForm.cleaned_data.get("dia")
            crear_viaje_hora= miForm.cleaned_data.get("hora")
            crear_viaje_ciudad= miForm.cleaned_data.get("ciudad")
            crear_viaje_codigo_viaje= miForm.cleaned_data.get("codigo_viaje")
            crear_viaje = Crear_Viaje(nombre_tutor=crear_viaje_nombre_tutor, 
                                      lugar=crear_viaje_lugar, 
                                      dia=crear_viaje_dia, 
                                      hora=crear_viaje_hora, 
                                      ciudad=crear_viaje_ciudad, 
                                      codigo_viaje=crear_viaje_codigo_viaje)
            crear_viaje.save()
            contexto = {"crear_viaje": Crear_Viaje.objects.all()}
            return render(request,'AppViajes/crear_viaje.html', contexto)
    else:
        miForm = crear_viajeForm()
    
    return render(request, "AppViajes/crear_viajeForm.html", {"form": miForm})

def participar_Form(request):
    if request.method == "POST":
        miForm = participarForm(request.POST)
        if miForm.is_valid():
            participar_codigo_viaje= miForm.cleaned_data.get("codigo_viaje")
            participar_nombre= miForm.cleaned_data.get("nombre")
            participar_apellido= miForm.cleaned_data.get("apellido")
            participar_email= miForm.cleaned_data.get("email")
            participar = Participar(codigo_viaje=participar_codigo_viaje,
                                    nombre=participar_nombre, 
                                    apellido=participar_apellido, 
                                    email=participar_email)
            participar.save()
            contexto = {"participar": Participar.objects.all()}
            return render(request,'AppViajes/participar.html', contexto)
    else:
        miForm = participarForm()
    
    return render(request, "AppViajes/participarForm.html", {"form": miForm})

def buscarViajes(request):
    return render(request, "AppViajes/buscar.html")

def encontrarViajes(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        crear_viaje = Crear_Viaje.objects.filter(ciudad__icontains=patron)
        contexto = {'crear_viaje':crear_viaje}
    else: 
        contexto = {"crear_viaje": Crear_Viaje.objects.all()}

    return render(request, "AppViajes/crear_viaje.html",contexto)