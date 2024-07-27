from django.urls import path, include
from AppViajes.views import *

urlpatterns = [
    path('',home, name="home"),
    path('proposito/',proposito, name="proposito"),
    
#Registrarse
    path('registrarse/',registrarse, name="registrarse"),
    path('registrarseForm/',registrarse_Form, name="registrarseForm"),

#Crear viaje   
    path('viaje/',viaje, name="viaje"),   
    path('viajeForm/',viaje_Form, name="viajeForm"),
    path('viajeUpdate/<id_viaje>/',viaje_Update, name="viajeUpdate"),
    path('viajeDelete/<id_viaje>/',viaje_Delete, name="viajeDelete"),
#Participar
    path('participar/',participar, name="participar"),
    path('participarForm/',participar_Form, name="participarForm"),
    path('participarUpdate/<id_participar>/',participar_Update, name="participarUpdate"),
    path('participarDelete/<id_participar>/',participar_Delete, name="participarDelete"),
    
#Buscar viajes    
    path('buscarViajes/',buscarViajes, name="buscarViajes"),
    path('encontrarViajes/',encontrarViajes, name="encontrarViajes"),

    ]