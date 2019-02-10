from django import forms

from .models import Lista_Compra

class Agregar_ldc_Form(forms.ModelForm):

    class Meta:

        model = Lista_Compra

        fields = [
            'usuario',
            'nombre',
            'local',
        ]

        labels = {
            'nombre': 'Nombre',
            'local': 'Local a comprar',
        }

        widgets = {
            'usuario': forms.HiddenInput,
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'local' : forms.Select(attrs = {'class':'form-control'}),
        }