from django.contrib import admin
from .models import Productos, Categorias, Tipo, Unidades_Medidas
# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    #Sirve para ver los campos a mostrar en la lista de productos
    list_display = ('nombre', 'precio_compra', 'precio_venta', 'usuario', 'categoria')

    #Agregar una barra de busqueda, por nombre y nombre de categoria, se pone __ para buscar desde otra tabla que tenga una referencia
    search_fields = ('nombre', 'categoria__nombre')

    #Agregar un filtrador en el lado derecho
    list_filter = ('categoria__nombre',)

    #Un filtro para fechas
    #date_hierarchy = 'fecha_publicacion'

    #Ordenar los campos por un factor
    ordering = ('nombre',)

    #Poner los campos de edicion
    #fields = ('usuario', 'nombre', 'categoria')

    #Otra forma de buscar claves foraneas
    raw_id_fields = ('usuario',)

    #Solo para que estos campos sean de lectura
    #readonly_fields = ('created', 'updated')

class CategoriasAdmin(admin.ModelAdmin):
    pass

class TipoAdmin(admin.ModelAdmin):
    pass

class Unidades_MedidasAdmin(admin.ModelAdmin):
    pass

admin.site.register(Productos, ProductosAdmin)
admin.site.register(Categorias, CategoriasAdmin)
admin.site.register(Unidades_Medidas, Unidades_MedidasAdmin)
admin.site.register(Tipo,TipoAdmin)