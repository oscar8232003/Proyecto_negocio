"""negocio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.urls import core_urlpatterns
from productos.urls import productos_urlpatterns
from registration.urls import registrarion_urlpatterns
from lista_compra.urls import lista_compra_urlpatterns
from django.conf import settings
#from productos_comprar.urls import productos_comprar_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('core.urls')),
    path('', include(core_urlpatterns)),
    path('productos/', include(productos_urlpatterns)),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/',include(registrarion_urlpatterns)),
    path('ldc/', include(lista_compra_urlpatterns)),


]

#Custom title for admin
admin.site.site_header = "Donde la señora ines"
admin.site.index_title = "Panel de administrador"
admin.site.site_title = "Donde la señora ines"

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)