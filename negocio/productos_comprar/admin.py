from django.contrib import admin
from .models import Productos_Comprar_Model
# Register your models here.

class Productos_Comprar_Admin(admin.ModelAdmin):
    pass

admin.site.register(Productos_Comprar_Model,Productos_Comprar_Admin)