from django import forms

from .models import Productos, Tipo, Categorias

class AgregarProductos(forms.ModelForm):

    class Meta:
        model = Productos

        fields = [
            'usuario',
            'nombre',
            'categoria',
            'precio_venta',
            'precio_compra',
            'promocion',
            'unidad_medida',
            'descripcion',
            'imagen',
        ]

        labels = {
            'nombre' : 'Nombre:',
            'categoria' : 'Categoria:',
            'precio_venta' : 'Precio de Venta:',
            'precio_compra' : 'Precio de Compra:',
            'promocion' : 'Promocion:',
            'unidad_medida' : 'Unidad de Medida:',
            'descripcion' : 'Descripcion:',
            'imagen': 'Imagen:',

        }
        widgets = {
            'usuario': forms.HiddenInput,
            'nombre' : forms.TextInput(attrs={'class':'form-control','placeholder':'ejem. Arroz aruba de 1/2kg'}),
            'categoria' : forms.Select(attrs={'class':'form-control'}),
            'precio_venta' : forms.TextInput(attrs={'class':'form-control'}),
            'precio_compra' : forms.TextInput(attrs={'class':'form-control'}),
            'promocion' : forms.Textarea(attrs={'class':'form-control','rows':2,}),
            'unidad_medida' : forms.Select(attrs={'class':'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control','rows':2,}),
            'imagen': forms.ClearableFileInput(attrs={'class':'form-control-file',}),

        }

class FormCategoria(forms.ModelForm):

    class Meta:

        model = Productos

        fields = [
            'categoria',
        ]

        labels = {
            'categoria': 'Categoria',
        }

        widgets = {
            'categoria': forms.Select(attrs={'class':'form-control'}),
        }

class FormTipo(forms.ModelForm):

    class Meta:

        model = Tipo

        fields = [
            'usuario',
            'nombre',
            'tipo',
        ]

        labels = {
            'usuario' : 'Usuario',
            'nombre' : 'Nombre',
            'tipo' : 'Tipo',
        }

        widgets = {
            'usuario' : forms.Select(),
            'nombre' : forms.TextInput(),
            'tipo' : forms.Select(),
        }
