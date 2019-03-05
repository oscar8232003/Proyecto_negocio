from django.contrib import admin
from .models import Inicio_banner, Inicio_titulo, Inicio_circulos, Inicio_cards, Inicio_foto_final, Footer, Productos_list, quiero_comprar

# Register your models here.
class admin_Inicio_banner(admin.ModelAdmin):
    list_display = ('__str__', 'activado',)


admin.site.register(Inicio_banner, admin_Inicio_banner)
admin.site.register(Inicio_titulo, admin_Inicio_banner)
admin.site.register(Inicio_circulos, admin_Inicio_banner)
admin.site.register(Inicio_cards, admin_Inicio_banner)
admin.site.register(Inicio_foto_final, admin_Inicio_banner)
admin.site.register(Footer, admin_Inicio_banner)
admin.site.register(Productos_list, admin_Inicio_banner)
admin.site.register(quiero_comprar, admin_Inicio_banner)

