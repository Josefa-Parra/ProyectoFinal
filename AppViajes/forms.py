from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class experienciaForm(forms.Form):
    nombre= forms.CharField(max_length=40,required=True)
    apellido= forms.CharField(max_length=40,required=True)
    ciudad= forms.CharField(max_length=40,required=True)
    comentario= forms.CharField(max_length=200,required=True)

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

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]