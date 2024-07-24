from django.urls import path, include
from AppViajes.views import *

urlpatterns = [
    path('',home, name="home"),
    path('proposito/',proposito, name="proposito"),
    path('registrarse/',registrarse, name="registrarse"),
    path('crear_viaje/',crear_viaje, name="crear_viaje"),
    path('participar/',participar, name="participar"),

    path('registrarseForm/',registrarse_Form, name="registrarseForm"),
    path('crear_viajeForm/',crear_viaje_Form, name="crear_viajeForm"),
    path('participarForm/',participar_Form, name="participarForm"),

    path('buscarViajes/',buscarViajes, name="buscarViajes"),
    path('encontrarViajes/',encontrarViajes, name="encontrarViajes"),

    ]