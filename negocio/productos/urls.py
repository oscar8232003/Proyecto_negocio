from django.urls import path
from .views import listar, detail, list_categoria, eliminar, crear, update, list_buscar



""""
urlpatterns =[
path('', index, name = "index" ),
]
"""

productos_urlpatterns = ([
path('list/', listar, name = "list" ),
path('detail/<slug:pk>', detail.as_view(), name = "detail" ),
path('list/categoria/<int:categoria>/', list_categoria, name = "list_categoria" ),
path('list/buscar/<slug:buscar>/', list_buscar, name = "list_buscar" ),
path('delete/<int:id>',eliminar , name = "eliminar" ),
path('agregar/', crear, name = "agregar"),
path('update/<int:id>', update, name = "update"),
], 'productos')

