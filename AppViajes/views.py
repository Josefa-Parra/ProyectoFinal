from django.shortcuts import render
from .models import *
from .forms import *

def home(request):
    return render(request,'AppViajes/index.html')

def proposito(request):
    return render(request,'AppViajes/proposito.html')

#Registrarse
def registrarse(request):
    contexto = {"registrarse": Registrarse.objects.all()}
    return render(request,'AppViajes/registrarse.html',contexto)

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
#Crear viaje
def viaje(request):
    contexto = {"viaje": Viaje.objects.all()}
    return render(request,'AppViajes/viaje.html',contexto)

def viaje_Form(request):
    if request.method == "POST":
        miForm = viajeForm(request.POST)
        if miForm.is_valid():
            viaje_nombre_tutor= miForm.cleaned_data.get("nombre_tutor")
            viaje_lugar= miForm.cleaned_data.get("lugar")
            viaje_dia= miForm.cleaned_data.get("dia")
            viaje_hora= miForm.cleaned_data.get("hora")
            viaje_ciudad= miForm.cleaned_data.get("ciudad")
            viaje_codigo_viaje= miForm.cleaned_data.get("codigo_viaje")
            viaje = Viaje(nombre_tutor=viaje_nombre_tutor, 
                                      lugar=viaje_lugar, 
                                      dia=viaje_dia, 
                                      hora=viaje_hora, 
                                      ciudad=viaje_ciudad, 
                                      codigo_viaje=viaje_codigo_viaje)
            viaje.save()
            contexto = {"viaje": Viaje.objects.all()}
            return render(request,'AppViajes/viaje.html', contexto)
    else:
        miForm = viajeForm()
    
    return render(request, "AppViajes/viajeForm.html", {"form": miForm})

def viaje_Update(request, id_viaje):
    viaje = Viaje.objects.get(id=id_viaje)
    if request.method == "POST":
        miForm = viajeForm(request.POST)
        if miForm.is_valid():
            viaje.nombre_tutor= miForm.cleaned_data.get("nombre_tutor")
            viaje.lugar= miForm.cleaned_data.get("lugar")
            viaje.dia= miForm.cleaned_data.get("dia")
            viaje.hora= miForm.cleaned_data.get("hora")
            viaje.ciudad= miForm.cleaned_data.get("ciudad")
            viaje.codigo_viaje= miForm.cleaned_data.get("codigo_viaje")
            viaje.save()
            contexto = {"viaje": Viaje.objects.all()}
            return render(request,'AppViajes/viaje.html', contexto)    
    else:
        miForm = viajeForm(initial={"nombre_tutor":viaje.nombre_tutor, 
                                      "lugar":viaje.lugar, 
                                      "dia":viaje.dia, 
                                      "hora":viaje.hora, 
                                      "ciudad":viaje.ciudad, 
                                      "codigo_viaje":viaje.codigo_viaje})
    return render(request, "AppViajes/viajeForm.html", {"form": miForm})

def viaje_Delete(request, id_viaje):
    viaje = Viaje.objects.get(id=id_viaje)
    viaje.delete()
    contexto = {"viaje": Viaje.objects.all()}
    return render(request, "AppViajes/viaje.html", contexto)


#Participar
def participar(request):
    contexto = {"participar": Participar.objects.all()}
    return render(request,'AppViajes/participar.html',contexto)

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

def participar_Update(request, id_participar):
    participar = Participar.objects.get(id=id_participar)
    if request.method == "POST":
        miForm = participarForm(request.POST)
        if miForm.is_valid():
            participar.codigo_viaje= miForm.cleaned_data.get("codigo_viaje")
            participar.nombre= miForm.cleaned_data.get("nombre")
            participar.apellido= miForm.cleaned_data.get("apellido")
            participar.email= miForm.cleaned_data.get("email")
            participar.save()
            contexto = {"participar": Participar.objects.all()}
            return render(request,'AppViajes/participar.html', contexto)    
    else:
        miForm = participarForm(initial={"codigo_viaje":participar.codigo_viaje,
                                    "nombre":participar.nombre, 
                                    "apellido":participar.apellido, 
                                    "email":participar.email})
    return render(request, "AppViajes/participarForm.html", {"form": miForm})

def participar_Delete(request, id_participar):
    participar = Participar.objects.get(id=id_participar)
    participar.delete()
    contexto = {"participar": Participar.objects.all()}
    return render(request, "AppViajes/participar.html", contexto)


#Buscar viajes
def buscarViajes(request):
    return render(request, "AppViajes/buscar.html")

def encontrarViajes(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        viaje = Viaje.objects.filter(ciudad__icontains=patron)
        contexto = {'viaje':viaje}
    else: 
        contexto = {"viaje": Viaje.objects.all()}

    return render(request, "AppViajes/viaje.html",contexto)