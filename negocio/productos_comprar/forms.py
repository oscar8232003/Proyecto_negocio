from django import forms
from .models import Productos_Comprar_Model

class Productos_Comprar_Form(forms.ModelForm):

    class Meta:

        model = Productos_Comprar_Model

        fields = [
            'cod_productos',
            'cod_lista_compras',
            'cantidad',
            'comentarios'
        ]

        labels = {
            'cod_productos':'Producto',
            'cantidad':'Cantidad',
            'comentarios':'Comentarios',
        }

        widgets = {
            'cod_lista_compras': forms.HiddenInput(),
            'cod_productos':forms.Select(attrs={'class':'form-control',}),
            'cantidad':forms.NumberInput(attrs={'class':'form-control',}),
            'comentarios':forms.Textarea(attrs={'rows':'3','class':'form-control',}),
        }