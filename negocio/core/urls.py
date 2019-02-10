from django.urls import path
from .views import index,quienes_somos, quiero_comprar



""""
urlpatterns =[
path('', index, name = "index" ),
]
"""


core_urlpatterns = ([
path('', index, name = "index" ),
path('quienes_somos/', quienes_somos, name = "quienes_somos" ),
path('quiero_comprar/', quiero_comprar, name = "quiero_comprar" ),
], 'core')

