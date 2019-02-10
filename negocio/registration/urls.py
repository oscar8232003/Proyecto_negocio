from django.urls import path
from .views import registro, sin_permiso, contacto

registrarion_urlpatterns = ([
    #path('registro/', registro, name = "registro"),
    path('permiso/', sin_permiso, name = "sin_permiso"),
    #path('contacto/', contacto, name = "contacto"),
                         ], 'registration')