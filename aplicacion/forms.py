from django import forms
from .models import User, Nucleos, Integrantes, DatosPersonales

class UserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password1']

class NucleosForm(forms.ModelForm):
    nombre = forms.CharField(label='Jefe de nucleo', required=True)
    integrantes = forms.CharField(label='Integrantes del nucleo', required=True)
    class Meta:
        model = Nucleos
        fields = ['nombre', 'integrantes']

class IntegrantesForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre y apellidos', required=True)
    class Meta:
        model = Integrantes
        fields = ['nombre']

class DatosPersonalesForm(forms.ModelForm):
    class Meta:
        model = DatosPersonales
        fields = ['carnet_ident', 'trabaja', 'estudia', 'desocupado', 'centro']
        