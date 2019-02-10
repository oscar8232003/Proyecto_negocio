from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
#from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django import forms
from .models import Productos_Comprar_Model
from .forms import Productos_Comprar_Form
from lista_compra.models import Lista_Compra
from productos.models import Productos, Tipo

@login_required(redirect_field_name='login')
def agregar_producto_comprar(request, id):
    tipo = Tipo.objects.get(usuario=request.user.id)
    if tipo.tipo == 'Interno' or tipo.tipo == 'Administrador':
        form = Productos_Comprar_Form()
        #Instanciamos la lista
        lista = Lista_Compra.objects.get(pk=id)
        id = str(id)
        if request.method == 'POST':
            form = Productos_Comprar_Form(request.POST)
            print(request.POST)
            #instanciamos el producto
            producto = Productos.objects.get(pk=int(request.POST['cod_productos']))
            #Sacamos el total del producto
            total_producto = int(request.POST['cantidad']) * producto.precio_compra
            #Creamos el objeto de productos_comprar, recuerda *****Para los campos de fk, tienes que traer el objeto completo para guardarlos, no sirve solalmente la id****
            pc = Productos_Comprar_Model(cod_productos=producto, cod_lista_compras = lista, cantidad = request.POST['cantidad'], total_producto = total_producto, comentarios= request.POST['comentarios'])
            if form.is_valid():
                pc.save()
                return HttpResponseRedirect('/ldc/detail_ldc/'+id+'?msg=crear_pc_ok')
            else:
                return HttpResponseRedirect('/ldc/detail_ldc/' +id+ '/agregar/?msg=crear_pc_error')
        else:
            return render(request, 'productos_comprar/agregar_productos_comprar.html', {'form':form,'lista':lista,})
    else:
        return redirect('registration:sin_permiso')


@login_required(redirect_field_name='login')
def detail_producto_comprar(request,id, id_pc):
    tipo = Tipo.objects.get(usuario=request.user.id)
    if tipo.tipo == 'Interno' or tipo.tipo == 'Administrador':
        pc = Productos_Comprar_Model.objects.get(pk = id_pc)
        id = id
        print(id_pc)
        return render(request, 'productos_comprar/detail_productos_comprar.html', {'object': pc, 'id':id })
    else:
        return redirect('registration:sin_permiso')

@login_required(redirect_field_name='login')
def update_producto_comprar(request,id, id_pc):
    tipo = Tipo.objects.get(usuario=request.user.id)
    if tipo.tipo == 'Interno' or tipo.tipo == 'Administrador':
        pc = Productos_Comprar_Model.objects.get(pk=id_pc)
        ldc = Lista_Compra.objects.get(pk = id)
        form = Productos_Comprar_Form(instance=pc)
        if request.method == 'POST':
            form = Productos_Comprar_Form(request.POST, instance=pc)
            id = str(id)
            producto = Productos.objects.get(pk=int(request.POST['cod_productos']))
            if form.is_valid():
                pc.cod_productos = producto
                pc.cod_lista_compras = ldc
                pc.cantidad = int(request.POST['cantidad'])
                pc.total_producto = producto.precio_compra * int(request.POST['cantidad'])
                pc.comentarios = request.POST['comentarios']
                pc.save()
                return HttpResponseRedirect('/ldc/detail_ldc/' + id + '?msg=upd_pc_ok')
            else:
                return HttpResponseRedirect('/ldc/detail_ldc/' + id + '?msg=upd_pc_error')
        else:
            return render(request, 'productos_comprar/update_productos_comprar.html', {'form': form, 'ldc': id, })
    else:
        return redirect('registration:sin_permiso')


@login_required(redirect_field_name='login')
def eliminar_producto_comprar(request,id, id_pc):
    tipo = Tipo.objects.get(usuario=request.user.id)
    if tipo.tipo == 'Interno' or tipo.tipo == 'Administrador':
        pc = Productos_Comprar_Model.objects.get(pk=id_pc)
        if request.method == 'POST':
            pc.delete()
            id = str(id)
            return HttpResponseRedirect('/ldc/detail_ldc/' + id + '?msg=eli_pc_ok')
        else:
            return render(request, 'productos_comprar/eliminar_productos_comprar.html', {'pc': pc, 'ldc': id, })
    else:
        return redirect('registration:sin_permiso')