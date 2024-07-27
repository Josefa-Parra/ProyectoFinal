from django import forms

class registrarseForm(forms.Form):
    nombre= forms.CharField(max_length=40,required=True)
    apellido= forms.CharField(max_length=40,required=True)
    email= forms.EmailField(required=True)
    ciudad= forms.CharField(max_length=40,required=True)

class viajeForm(forms.Form):
    nombre_tutor= forms.CharField(max_length=40,required=True, label="Nombre de Tutor")
    lugar= forms.CharField(max_length=40,required=True)
    dia= forms.DateField(required=True)
    hora= forms.CharField(max_length=40,required=True)
    ciudad= forms.CharField(max_length=40,required=True)
    codigo_viaje= forms.CharField(max_length=40,required=True, label="Codigo de Viaje")

class participarForm(forms.Form):
    codigo_viaje= forms.CharField(max_length=40,required=True, label="Codigo de Viaje")
    nombre= forms.CharField(max_length=40,required=True)
    apellido= forms.CharField(max_length=40,required=True)
    email= forms.EmailField(required=True)