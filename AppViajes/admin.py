from django.contrib import admin

# Register your models here.
from .models import *

class ExperienciaAdmin(admin.ModelAdmin):
    list_display= ("nombre","apellido","ciudad","comentario")
    list_filter= ("nombre",)

class ViajeAdmin(admin.ModelAdmin):
    list_display= ("nombre_tutor","lugar","dia","hora","ciudad","codigo_viaje")
    list_filter= ("nombre_tutor",)

class ParticiparAdmin(admin.ModelAdmin):
    list_display= ("codigo_viaje","nombre","apellido","email")
    list_filter= ("codigo_viaje",)

admin.site.register(Experiencia,ExperienciaAdmin)
admin.site.register(Viaje,ViajeAdmin)
admin.site.register(Participar,ParticiparAdmin)