from django.db import models

class Experiencia(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    ciudad= models.CharField(max_length=40)
    comentario= models.CharField(max_length=200)

    class Meta:
        ordering = ["apellido","nombre"]

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
                                                      
class Viaje(models.Model):
    nombre_tutor= models.CharField(max_length=40)
    lugar= models.CharField(max_length=40)
    dia= models.DateField()
    hora= models.CharField(max_length=40)
    ciudad= models.CharField(max_length=40)
    codigo_viaje= models.CharField(max_length=40)

    class Meta:
        ordering = ["codigo_viaje","nombre_tutor"]

    def __str__(self):
        return f"{self.codigo_viaje}, {self.nombre_tutor}"
    
class Participar(models.Model):
    codigo_viaje= models.CharField(max_length=40)
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()

    class Meta:
        verbose_name ="Participar"
        verbose_name_plural ="Participantes"
        ordering = ["codigo_viaje","apellido","nombre"]

    def __str__(self):
        return f"{self.codigo_viaje}, {self.apellido}, {self.nombre}"