from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'AppViajes/index.html')

def proposito(request):
    return render(request,'AppViajes/proposito.html')

#Comentarios
@login_required
def experiencia(request):
    contexto = {"experiencia": Experiencia.objects.all()}
    return render(request,'AppViajes/experiencia.html',contexto)

@login_required
def Experiencia_Form(request):
    if request.method == "POST":
        miForm = experienciaForm(request.POST)
        if miForm.is_valid():
            experiencia_nombre= miForm.cleaned_data.get("nombre")
            experiencia_apellido= miForm.cleaned_data.get("apellido")
            experiencia_ciudad= miForm.cleaned_data.get("ciudad")
            experiencia_comentario= miForm.cleaned_data.get("comentario")
            experiencia = Experiencia(nombre=experiencia_nombre, 
                                      apellido=experiencia_apellido,  
                                      ciudad=experiencia_ciudad,
                                      comentario=experiencia_comentario)
            experiencia.save()
            contexto = {"experiencia": Experiencia.objects.all()}
            return render(request,'AppViajes/experiencia.html', contexto)
    else:
        miForm = experienciaForm()
    
    return render(request, "AppViajes/experienciaForm.html", {"form": miForm})
#Crear viaje
@login_required
def viaje(request):
    contexto = {"viaje": Viaje.objects.all()}
    return render(request,'AppViajes/viaje.html',contexto)

@login_required
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

@login_required
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

@login_required
def viaje_Delete(request, id_viaje):
    viaje = Viaje.objects.get(id=id_viaje)
    viaje.delete()
    contexto = {"viaje": Viaje.objects.all()}
    return render(request, "AppViajes/viaje.html", contexto)


#Participar
@login_required
def participar(request):
    contexto = {"participar": Participar.objects.all()}
    return render(request,'AppViajes/participar.html',contexto)

@login_required
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

@login_required
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

@login_required
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

#Login/Logout

def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request,user)
            return render(request, "AppViajes/index.html", {"mensaje":f"Bienvenido {usuario}"} )
        else:
            return redirect(reverse_lazy('login'), {"mensaje":"Error, datos incorrectos"} )
    else:
        miForm = AuthenticationForm()

    return render(request,"AppViajes/login.html", {"form": miForm})

def register(request):
    if request.method == 'POST':
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))   
    else:
            miForm = RegistroForm()

    return render(request,"AppViajes/registro.html", {"form": miForm})
