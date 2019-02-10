from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):

    class Meta:
        model = User

        fields = [
            'first_name',
            'username',
            'password1',
            'password2',
        ]


class ContactoForm(forms.Form):

    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Ingrese el nombre'}
    ), min_length=3, max_length=100)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Ingrese el email'}
    ), min_length=3, max_length=100)
    content =  forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows':3, 'placeholder':'Ingrese el mensaje'}
    ), min_length=3, max_length=100)
