from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, reverse
from .models import Productos, Categorias, Tipo
from .form import AgregarProductos, FormCategoria
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator



#Metodo Listar VBF con Filtrado de metodo POST
#Se incorporo hasta ahora el metodo filtrar por categoria o por nombre
def listar(request):
    #usuario = Tipo.objects.get(usuario=request.user.id)
    #print(usuario.tipo)
        if request.method == 'POST':
            categoria = request.POST.get('categoria', None)
            buscar = request.POST.get('buscar', None)
            print(request.POST)
            if categoria is not None:
                #Otra forma de buscar es no poner la url completa como la de buscar
                return HttpResponseRedirect('/productos/list/categoria/' + categoria)
            else:
                return HttpResponseRedirect('/productos/list/buscar/' + buscar)
        else:
            Listado = Productos.objects.exclude(categoria__nombre = 'Vega')
            form = FormCategoria()
            paginator = Paginator(Listado, 10)
            page = request.GET.get('page')
            Listado_nuevo = paginator.get_page(page)
            return render(request, 'productos/listar.html', {'productos': Listado_nuevo, 'form': form})


"""

# Metodo Listar VBF con Filtrado de metodo GET
def listar(request):
    print(request.user.id)
    categoria = request.GET.get('categoria', None)
    if categoria is not None:
        return HttpResponseRedirect('/list/'+categoria)
    else:
        Listado = Productos.objects.all()
        form = FormCategoria()
        return render(request, 'core/listar.html', {'productos': Listado, 'form': form})
"""

"""
#Metodo listar pero con VBC
class listar(ListView):
    model = Productos
    template_name = "core/listar.html"

    def get_queryset(self):
        queryset = super(listar, self).get_queryset()
        return queryset.filter(nombre__contains = '')
"""


#Metodo detail con VBF
def detail(request, id):
    objeto = get_object_or_404(Productos, pk=id)
    precio_estimado=0
    if objeto:
        precio_estimado = int(objeto.precio_compra) * 1.3
    return render(request, 'productos/detail.html', {'object':objeto, 'precio_estimado':int(precio_estimado)})
"""
#Metodo detail con VBC
class detail(DetailView):
    model = Productos
    template_name = "productos/detail.html"
"""

#Metodo filtro de categoria con VBF
def list_categoria(request, categoria):
        objeto = Productos.objects.filter(categoria = categoria)
        form = FormCategoria()
        paginator = Paginator(objeto, 10)
        page = request.GET.get('page')
        Listado_nuevo = paginator.get_page(page)
        return render(request, 'productos/listar.html', {'productos':Listado_nuevo, 'form':form})

#Metodo filtro de buscar con VBF
def list_buscar(request, buscar):
        objeto = Productos.objects.filter(nombre__contains = buscar)
        form = FormCategoria()
        paginator = Paginator(objeto, 10)
        page = request.GET.get('page')
        Listado_nuevo = paginator.get_page(page)
        return render(request, 'productos/listar.html', {'productos':Listado_nuevo, 'form':form})

#Metodo eliminar con VBF
@login_required(redirect_field_name='login')
def eliminar(request, id):
    tipo = Tipo.objects.get(usuario=request.user.id)
    if tipo.tipo == 'Interno' or tipo.tipo == 'Administrador':
        objeto = Productos.objects.get(id=id)
        if request.method == 'POST':
            objeto.delete()
            return redirect(reverse('productos:list')+"?msg=eli_ok")
        else:
            return render(request, 'productos/eliminar.html', {'productos': objeto,})
    else:
        return redirect('registration:sin_permiso')

#Metodo Crear con VBF
@login_required(redirect_field_name='login')
def crear(request):
    tipo = Tipo.objects.get(usuario=request.user.id)

    if tipo.tipo == 'Interno' or tipo.tipo == 'Administrador':
        if request.method == 'POST':
            form = AgregarProductos(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect(reverse('productos:list')+"?msg=crear_ok")
            else:
                return redirect(reverse('productos:agregar') +"?msg=crear_error")
        else:
            form = AgregarProductos()
        return render(request, 'productos/agregar.html', {'form':form})
    else:
        return redirect('registration:sin_permiso')

#Metodo Update con VBF
@login_required(redirect_field_name='login')
def update(request, id):
    tipo = Tipo.objects.get(usuario=request.user.id)

    if tipo.tipo == 'Interno' or tipo.tipo == 'Administrador':
        producto = Productos.objects.get(id=id)
        if request.method == 'POST':
            form = AgregarProductos(request.POST, request.FILES, instance=producto)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/productos/list?msg=upd_ok')
            else:
                return HttpResponseRedirect('/productos/list?msg=upd_error')
        else:
            form = AgregarProductos(instance=producto)
            return render(request, 'productos/update.html', {'form':form})
    else:
        return redirect('registration:sin_permiso')