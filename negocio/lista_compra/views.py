from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Lista_Compra
from productos_comprar.models import Productos_Comprar_Model
from .forms import Agregar_ldc_Form
from django.db.models.aggregates import Sum
from productos.models import Tipo
from django.core.paginator import Paginator


"""
LA FUNCION LISTA_LDC SE ENCARGA DE LISTAR LAS LISTAS DE COMPRAS EN SU TOTALIDAD, VERIFICA SI ESTAS LOGEADOS SINO TE REDIRIGE AL LOGIN, DESPUES TE VERIFICA TU TIPO DE USUARIO, DEPENDIENDO SI ERES
INTERNO O ADMINISTRADOR TE DEJA ENTRAR SINO TE REDIRIGE A UNA VISTA SIN PERMISOS, DESPUES DE TODAS LAS VALIDACIONES, VERIFICA SI ERES ADMINISTRADOR, SI ES ASI TIENES DERECHO DE ENTRAR A TODAS LAS LISTAS
SINO SOLAMENTE PODRAS VER TUS LISTAS DE COMPRAS, TAMBIEN SE ENCARGA DE SUMAR LAS LISTAS DE COMPRAS SELECCIONADAS VERIFICA SI SE HIZO UNA PETICION POST CON MAS DE 1 OBJETO, CABE RECALCAR QUE EN LAS PETICIONES SIEMPRE
VA A HABER 1 OBJETO YA QUE POR TEMAS DE SEGURIDAD, EN EL FORM HAY QUE MANDAR UNA KEY VALIDADORA DEL FORM PARA SEGURIDAD INTERNA, EN EL CASO QUE SEA MAS DE 1 OBJETO, ESTE HACE UN FOR VERIFICANDO QUE EL OBJETO NO SEA
EL TOKEN, SI NO ES EL TOKEN, SE BUSCA SU VALOR POR SU PK Y LO SUMA A UNA VARIABLE LLAMADA SUMA_LISTA, AGREGAR TAMBIEN QUE SE TIENE UN PAGINADOR PARA MOSTRAR 8 OBJETOS POR PAGINA, AL TERMINAR SE HACE UN RENDER CON EL TEMPLATE
LISTAR CON LOS DICCIONARIOS DE LOS OBJETOS DE EL PAGINADOR Y EL TOTAL DE LAS LISTAS SUMADAS.
"""

@login_required(redirect_field_name='login')
def lista_ldc(request):
    tipo = Tipo.objects.get(usuario=request.user.id)
    if tipo.tipo == 'Interno' or tipo.tipo == 'Administrador':
        if request.user.is_superuser:
            listas = Lista_Compra.objects.all()
        else:
            listas = Lista_Compra.objects.filter(usuario = request.user.id)

        suma_lista = 0
        if request.method == 'POST':
            if len(request.POST) > 1:
                for obj in request.POST:
                    if not obj == "csrfmiddlewaretoken":
                        lista_provisioria=Lista_Compra.objects.get(pk = obj)
                        suma_lista+=lista_provisioria.total_lista
        paginator = Paginator(listas, 8)
        page = request.GET.get('page')
        Listas = paginator.get_page(page)
        return render(request, 'lista_compra/listar.html', {'listas':Listas, 'suma_lista':suma_lista})
    else:
        return redirect('registration:sin_permiso')

"""
EN ESTA FUNCION TAMBIEN PEDIMOS QUE ESTE REGISTRADO EL USUARIO SINO LO MANDARA AL LOGIN, TAMBIEN VERIFICA EL TIPO SI ES INTERNO O ADMINISTRADOR QUE ES SACADO DE LA TABLA TIPO, ADEMAS SE IMPORTA LA CLASE DEL FORMULARIO Y 
ES ASIGANADA A LA VARIABLE FORM, SI LLEGASE HABER UNA PETICION TIPO POST, SE HACE LA VERIFICACION, SI ES ASI, SE VERIFICA QUE EL LLENADO EL FORMULARIO ESTE CORRECTO Y SE PROCEDE A REDIRECCIONAR A UNA PAGINA CON UN MENSAJE DE 
EXITO, EN EL CASO DE QUE NO ESTE CORRECTO, SE REDIRIGE A OTRO TEMPLATE CON UN MENSAJE DE ERROR, SI EN EL CARO QUE NO UBIESE UNA PETICION DE TIPO POST SOLAMENTE SE RENDERIZA EL TEMPLATE CON EL DICCIONARIO QUE CONTIENE EL 
FOMULARIO.
"""

@login_required(redirect_field_name='login')
def agregar_ldc(request):
    tipo = Tipo.objects.get(usuario=request.user.id)
    if tipo.tipo == 'Interno' or tipo.tipo == 'Administrador':
        form = Agregar_ldc_Form()
        if request.method == 'POST':
            lista = Agregar_ldc_Form(request.POST)
            if lista.is_valid():
                lista.save()
                return redirect(reverse('lista_compra:list_ldc')+"?msg=crear_ldc_ok")
            else:
                return HttpResponseRedirect('/ldc/agregar_ldc/'+"?msg=crear_ldc_error")
        else:
            return render(request, 'lista_compra/agregar_ldc.html', {'form':form})
    else:
        return redirect('registration:sin_permiso')

"""
EN ESTA FUNCION OCURRE LO MISMO QUE LAS ANTERIORES, SE PIDE UN USUARIO LOGUEADO CON FUNCIONES DE INTERNO O ADMINISTRADOR, ESTA VIEW ES UN ACTUALIZAR POR ENDE PRIMERO SE BUSCA EL OBJETO QUE PERTENESZA A LA ID SOLICITADA, 
DESPUES SE NECESITA TRAER EL FORMULARIO LLENADO ANTERIORMENTE, PARA ESO SE INSTANCIA EL FORM, PRIMERO SE OTORGA A UNA VARIABLE EL OBJ TRAIDO Y A OTRA VARIABLE EL FORM CON UNA INSTANCIA DEL OBJETO COMO PARAMETRO, EN EL CASO QUE 
SE HAGA UNA PETICION DE TIPO POST, SE OTORGA A UNA VARIABLE EL FORM LLENADO CON EL REQUEST.POST Y INSTANCIADO AL OBJETO OBTENIDO ANTERIORMENTE, SE VERIFICA QUE EL FORMULARIO LLENADO ESTE CORRECTO Y SE PROCEDE A GUARDARLO EN LA 
BD SINO SE REDIRIGE A UN TEMPLATE CON UN ERROR, EN EL CASO QUE ESTE TODO BIEN SE REDIRIGE A UN TEMPLATE CON UN MENSAJE DE EXITO, EN EL CASO QUE SE HAGA UNA PETICION DE TIPO POST, ESTE SOLAMENTE LLENADA EL FORMULARIO INSTANCIADO 
CON EL OBJETO QUE SE TIENE QUE TRAER PARA PODER LLENAR EL FORMULARIO CON LOS DATOS PREVIAMENTE PROPORCIONADOS. 
"""

@login_required(redirect_field_name='login')
def update_ldc(request, id):
    tipo = Tipo.objects.get(usuario=request.user.id)
    if tipo.tipo == 'Interno' or tipo.tipo == 'Administrador':
        lista = Lista_Compra.objects.get(pk=id)
        form = Agregar_ldc_Form(instance=lista)
        if request.method == 'POST':
            form = Agregar_ldc_Form(request.POST, instance=lista)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/ldc/list/' + '?msg=upd_ldc_ok')
            else:
                return HttpResponseRedirect('/ldc/list/' + '?msg=upd_ldc_error')
        else:
            return render(request, 'lista_compra/update_ldc.html', {'form':form})
    else:
        return redirect('registration:sin_permiso')

"""
EN ESTA FUNCION OCURRE LO MISMO QUE LAS ANTERIORES, SE PIDE UN USUARIO LOGUEADO CON FUNCIONES DE INTERNO O ADMINISTRADOR, EN ESTA VIEW SE ENCARGA DE ELIMINAR UN OBJETO CON UNA PETICION POST PASANDO COMO PARAMETRO LA ID DEL OBJETO 
A ELIMINAR.
"""

@login_required(redirect_field_name='login')
def eliminar_ldc(request, id):
    tipo = Tipo.objects.get(usuario=request.user.id)
    if tipo.tipo == 'Interno' or tipo.tipo == 'Administrador':
        ldc = Lista_Compra.objects.get(pk=id)
        if request.method == 'POST':
            ldc.delete()
            return redirect(reverse('lista_compra:list_ldc')+"?msg=eli_ldc_ok")
        else:
            return render(request, 'lista_compra/eliminar_ldc.html', {'ldc': ldc})
    else:
        return redirect('registration:sin_permiso')


"""
EN ESTA FUNCION OCURRE LO MISMO QUE LAS ANTERIORES, SE PIDE UN USUARIO LOGUEADO CON FUNCIONES DE INTERNO O ADMINISTRADOR, EN ESTA VIEW PRETENDEMOS TRAER TODOS LOS PRODODUCTOS LIGADOS A ESTA LISTA, POR ENDE PRIMERO SE NECESITA 
TRAER LOS PRODUCTOS CON LA ID DE LA LISTA, ESTOS SON ASIGANDOS A UNA VARIABLE LLAMADA PRODUCTOS QUE CONTENDRA UN ARRAY CON LOS OBJETOS, DESPUES SE VERIFICA SI EXISTEN PRODUCTOS PARA DICHA LISTA, EN EL CASO QUE NO UBIERAN SE REDIRIGE A 
OTRO TEMPLATE CON UNA INTERFAZ DE LISTA VACIA, EN EL CASO QUE SI TUBIERA, SE HACE UNA SUMATORIA A TODOS LOS PRODUCTOS QUE TENGAN UN VALOR EN TOTAL_PRODUCTO Y SE GUARDA EN EL TOTAL DE LA LISTA, EN EL CASO QUE SE NECESITE 
UNA PETICION DE TIPO POST, ESTE HACE UN FOR EN LOS PRODUCTOS PARA PONERLOS EN FALSE, YA QUE SE TIENE UN VALIDADOR QUE LOS PRODUCTOS FUERON COMPRADOS O NO, POR ENDE SE DEJAN EN FALSE Y SE GUARDAN, EN EL CASO QUE EL FORM MANDE 
MAS DE 1 OBJETO, ESTE SE EMPIEZAN A GUARDAN EN UNA LISTA Y SE ELIMINA EL PRIMERO YA QUE ES EL TOKEN DE VALIDACION DEL FORM DE DJANGO, AHORA SE VERIFICA LOS OBJETOS QUE FUERON MARCADOS Y SE CAMBIAN A TRUE PROSEGUIENDO A GUARDARLOS 
Y REDIRECCIONANDOLOS A EL TEMPLATE DE LISTAS.
"""
@login_required(redirect_field_name='login')
def detail_ldc(request,id):
    tipo = Tipo.objects.get(usuario=request.user.id)
    if tipo.tipo == 'Interno' or tipo.tipo == 'Administrador':
        lista = Lista_Compra.objects.get(pk = id)
        productos = Productos_Comprar_Model.objects.filter(cod_lista_compras = id)
        if productos.exists():
            total = productos.aggregate(Sum('total_producto'))
            lista.total_lista = total['total_producto__sum']
            lista.save()
            list=[]
            if request.method == 'POST':
                for prod in productos:
                    prod.estado_producto = 0
                    prod.save()
                if len(request.POST) > 1 :
                    for obj in request.POST:
                        list.append(obj)
                    list.pop(0)
                    for obj2 in list:
                        modificar = Productos_Comprar_Model.objects.get(pk=obj2)
                        modificar.estado_producto = 1
                        modificar.save()
                    return redirect(reverse('lista_compra:list_ldc')+"?msg=select_ldc_ok")
        return render(request, 'lista_compra/detail_ldc.html', {'ldc': lista, 'productos':productos})
    else:
        return redirect('registration:sin_permiso')