from django.urls import path, include
from AppViajes.views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',home, name="home"),
    path('proposito/',proposito, name="proposito"),
    
#Comentarios
    path('experiencia/',experiencia, name="experiencia"),
    path('experienciaForm/',Experiencia_Form, name="experienciaForm"),

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

#login/registro/logout
    path('login/',loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="AppViajes/logout.html"), name="logout"),
    path('registro', register, name='registro'),
]