from django import forms

from .models import Usuario

class UsuarioForms(forms.ModelForm):

    class Meta:

        model = Usuario
        fields = ['nombre', 'apellido']


