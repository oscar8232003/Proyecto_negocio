from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Lista_Compra
from productos_comprar.models import Productos_Comprar_Model
from .forms import Agregar_ldc_Form
from django.db.models.aggregates import Sum
from productos.models import Tipo
from django.core.paginator import Paginator

#Sirve para listar las ldc
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

#Agregar ldc
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


#Updatear lista de compras
#El instance es para rellenar un formulario
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


#Eliminar una lista de compras
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

#Detail de las listas
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