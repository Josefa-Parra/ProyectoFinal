from django.db import models

class Registrarse(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()
    ciudad= models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nombre}"
                                                      
class Crear_Viaje(models.Model):
    nombre_tutor= models.CharField(max_length=40)
    lugar= models.CharField(max_length=40)
    dia= models.DateField()
    hora= models.CharField(max_length=40)
    ciudad= models.CharField(max_length=40)
    codigo_viaje= models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.nombre_tutor},{self.codigo_viaje}"
    
class Participar(models.Model):
    codigo_viaje= models.CharField(max_length=40)
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()

    class Meta:
        verbose_name ="Participar"
        verbose_name_plural ="Participantes"

    def __str__(self):
        return f"{self.apellido},{self.codigo_viaje}"