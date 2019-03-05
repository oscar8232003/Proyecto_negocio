from django.shortcuts import render
from productos.models import Tipo

"""
FUNCION INDEX, LA CUAL SE ENCARGA DE VERIFICAR SI EL USUARIO ESTA REGISTRADO, SI ES ASI BUSCA EN LA TABLA TIPO PARA ASIGNARLE SU TIPO DE USUARIO,
ESTE LO ASIGNA A LA SESION "TIPO" SINO ESTE TIENE POR DEFECTO LA SESSION "NONE".



"""


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