from django.urls import path, include
from AppViajes.views import *

urlpatterns = [
    path('',home, name="home"),
    path('proposito/',proposito, name="proposito"),
    path('registrarse/',registrarse, name="registrarse"),
    path('crear_viaje/',crear_viaje, name="crear_viaje"),
    path('participar/',participar, name="participar"),

]