from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .form import RegistroForm, ContactoForm
from django import forms
from django.shortcuts import redirect, reverse
from django.core.mail import EmailMessage
# Create your views here.

#Funcion para el registro
def registro(request):
    form = RegistroForm()
    form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre de usuario'})
    form.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre'})
    form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Contraseña'})
    form.fields['password2'].widget = forms.PasswordInput( attrs={'class': 'form-control mb-2', 'placeholder': 'Repitela Contraseña'})

    if request.method == 'POST':
        form_registro = RegistroForm(request.POST)
        validar = User.objects.filter(username = request.POST['username']).exists()
        if not validar:
            if form_registro.is_valid():
                form_registro.save()
                return HttpResponseRedirect('/accounts/login/?msg=correcto')
        else:
            return HttpResponseRedirect('/accounts/registro/?msg=error_existe')
    return render(request, 'registration/registro.html', {'form':form})

def sin_permiso(request):
    return render(request, 'registration/sin_permiso.html')

def contacto(request):
    form_contacto = ContactoForm()
    if request.method == "POST":
        form_contacto = ContactoForm(request.POST)
        if form_contacto.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y redirecionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["nerd.16@hotmail.cl"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('registration:contacto') + "?ok")
            except:
                return redirect(reverse('registration:contacto') + "?fail")
    return render(request, 'registration/contacto.html', {'form':form_contacto})
