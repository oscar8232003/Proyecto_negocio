from django.db import models
from django.contrib.auth.models import User
from productos.models import Productos
from lista_compra.models import Lista_Compra
# Create your models here.

class Productos_Comprar_Model(models.Model):
    cod_productos = models.ForeignKey(Productos, on_delete=models.CASCADE, blank=True, null=True)
    cod_lista_compras = models.ForeignKey(Lista_Compra, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0, verbose_name="cantidad", blank=True, null=True)
    total_producto = models.PositiveIntegerField(default=0, verbose_name="total")
    comentarios = models.TextField(blank=True, null=True, verbose_name="comentarios")
    estado_producto = models.BooleanField(default=False, verbose_name="Estado del Producto")

    class Meta:
        verbose_name = "Producto a Comprar"
        verbose_name_plural= "Productos a Comprar"
        db_table = "Productos_Comprar"

    def __str__(self):
        return "{}, ${} por {}".format(self.cod_productos.nombre, self.cod_productos.precio_compra, self.cod_productos.unidad_medida.medida)