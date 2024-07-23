from django.contrib import admin

# Register your models here.
from .models import *

class RegistrarseAdmin(admin.ModelAdmin):
    list_display= ("nombre","apellido","email","ciudad")
    list_filter= ("nombre",)

class Crear_ViajeAdmin(admin.ModelAdmin):
    list_display= ("nombre_tutor","lugar","dia","hora","ciudad","codigo_viaje")
    list_filter= ("nombre_tutor",)

class ParticiparAdmin(admin.ModelAdmin):
    list_display= ("codigo_viaje","nombre","apellido","email")
    list_filter= ("codigo_viaje",)

admin.site.register(Registrarse,RegistrarseAdmin)
admin.site.register(Crear_Viaje,Crear_ViajeAdmin)
admin.site.register(Participar,ParticiparAdmin)