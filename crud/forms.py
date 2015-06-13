from django import forms
from models import Usuarios

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields =  '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Twitter'})

        }