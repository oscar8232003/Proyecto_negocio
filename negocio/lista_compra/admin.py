from django.contrib import admin
from .models import Lista_Compra, Locales
# Register your models here.

class Lista_Compra_Admin(admin.ModelAdmin):
    readonly_fields = ('total_lista',)

class Locales_Admin(admin.ModelAdmin):
    pass


admin.site.register(Lista_Compra,Lista_Compra_Admin)
admin.site.register(Locales,Locales_Admin)