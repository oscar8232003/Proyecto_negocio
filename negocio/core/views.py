from django.shortcuts import render
from productos.models import Tipo


# Create your views here.

def index(request):

    if request.user.id is not None:
        persona = Tipo.objects.get(usuario = request.user.id)
        request.session['tipo']= persona.tipo
    else:
        request.session['tipo']="None"

    #for key, value in request.session.items():
    #    print('{} => {}'.format(key, value))
    return render(request, 'core/index.html')

def quienes_somos(request):
    return render(request, 'core/quienes_somos.html')

def quiero_comprar(request):
    return render(request, 'core/quiero_comprar.html')