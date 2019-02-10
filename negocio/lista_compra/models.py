from django.db import models
from django.contrib.auth.models import User


class Locales(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False, verbose_name="Nombre")
    logo = models.ImageField(upload_to='lista_compra/', null=True, blank=True, default="/media/core/sin-imagen.png")

    class Meta:
        db_table = "Locales"
        ordering = ["nombre"]
        verbose_name_plural = "Locales"
        verbose_name = "Local"

    def __str__(self):
        return self.nombre

class Lista_Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(verbose_name="Nombre", max_length=100, null=True, blank=True)
    local = models.ForeignKey(Locales, on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)
    total_lista = models.IntegerField(default=0, verbose_name="Total")

    class Meta:
        db_table = "Lista_Compra"
        ordering = ["-fecha"]
        verbose_name = "Lista de compras"
        verbose_name_plural = "Listas de compras"

    def __str__(self):
        return self.nombre