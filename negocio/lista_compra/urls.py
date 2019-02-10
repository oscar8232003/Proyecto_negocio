from django.urls import path
from .views import lista_ldc, agregar_ldc, update_ldc, eliminar_ldc, detail_ldc
from productos_comprar.views import agregar_producto_comprar, detail_producto_comprar,update_producto_comprar, eliminar_producto_comprar

lista_compra_urlpatterns = ([
    path('list/', lista_ldc, name = "list_ldc"),
    path('agregar_ldc/',agregar_ldc, name = "Agregar_ldc"),
    path('update_ldc/<int:id>', update_ldc, name = "updatear_ldc"),
    path('borrar_ldc/<int:id>', eliminar_ldc, name= "borrar_ldc"),
    path('detail_ldc/<int:id>', detail_ldc, name= "detail_ldc"),
    path('detail_ldc/<int:id>/agregar/', agregar_producto_comprar, name="agregar_pc"),
    path('detail_ldc/<int:id>/editar/<int:id_pc>', update_producto_comprar, name="editar_pc"),
    path('detail_ldc/<int:id>/eliminar/<int:id_pc>', eliminar_producto_comprar, name="eliminar_pc"),
    path('detail_ldc/<int:id>/detail/<int:id_pc>', detail_producto_comprar, name="detail_pc"),
    ],'lista_compra')