from django.db import models
from django.contrib.auth.models import User



class Categorias(models.Model):
    nombre = models.CharField(verbose_name="Nombre categoria", max_length=100)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre

class Unidades_Medidas(models.Model):
    medida = models.CharField(verbose_name="Medida",max_length=50)

    class Meta:
        verbose_name = "Unidades de Medida"
        verbose_name_plural = "Unidades de Medidas"
        ordering = ['medida']

    def __str__(self):
        return self.medida

#Elimina la imagen anterior *SIN OCUPAR AUN*
def custom_upload_to(instance, filename):
    old_instance = Productos.objects.get(pk=instance.pk)
    old_instance.imagen.delete()
    return 'productos/'+filename

class Productos(models.Model):
    usuario = models.ForeignKey(User, on_delete= models.CASCADE)
    nombre = models.CharField(verbose_name= "Nombre", max_length= 100, null=True, blank=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, null=True, blank=True)
    precio_venta = models.IntegerField(verbose_name= "Precio venta", default=0, null=True, blank=True)
    precio_compra = models.IntegerField(verbose_name= "Precio compra",default=0, null=True, blank=True)
    promocion = models.TextField(verbose_name="Promocion", blank= True, null=True)
    unidad_medida = models.ForeignKey(Unidades_Medidas, on_delete= models.CASCADE, null=True, blank=True)
    descripcion = models.TextField(verbose_name= "Descripcion", blank=True, null=True)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True, default="core/sin-imagen.png")
    fecha_actualizacion = models.DateField(verbose_name="Fecha de Actualizacion", auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']

    #Este es para que valor se muestre en la lista, sino semuestra un objects Productos(1)
    def __str__(self):
        return "{}".format(self.nombre)


class Tipo(models.Model):
    tipos = (
        ('Administrador','Administrador'),
        ('Interno', 'Interno'),
        ('Vendedor', 'Vendedor'),
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(verbose_name="Nombre", max_length=100, blank=True, null=True)
    tipo = models.CharField(verbose_name="Tipo", max_length=100,choices=tipos, default='Vendedor')

    class Meta:
        verbose_name = "Tipo de Cliente"
        verbose_name_plural = "Tipos de Clientes"
        ordering = ['tipo']

    #Este es para que valor se muestre en la lista, sino semuestra un objects Productos(1)
    def __str__(self):
        return "{}".format(self.usuario.username)


class Analisis_datos(models.Model):
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    nombre_producto =models.CharField(verbose_name="Nombre", max_length=100, blank=True, null=True)
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad", default = 0)
    precio_compra = models.PositiveIntegerField(verbose_name="Precio Compra", default = 0)
    precio_venta_actual = models.PositiveIntegerField(verbose_name="Precio Venta", default = 0)
    precio_estimado_15 = models.PositiveIntegerField(verbose_name="Precio Venta con 15%", default = 0)
    precio_estimado_30 = models.PositiveIntegerField(verbose_name="Precio Venta con 30%", default = 0)
    ganancia_precio_actual = models.PositiveIntegerField(verbose_name="Ganancia por productos actual", default=0)
    ganancia_estimada_15 = models.PositiveIntegerField(verbose_name="Ganancia por productos con 15%", default = 0)
    ganacia_estimada_30 = models.PositiveIntegerField(verbose_name="Ganancia por productos con 30%", default = 0)
    total_producto_actual = models.PositiveIntegerField(verbose_name="Total valor del producto", default = 0)
    fecha_creacion =  models.DateField(auto_now=True, verbose_name="Fecha de Creacion")
    local =models.CharField(verbose_name="Local", max_length=100, blank=True, null=True)
    estado = models.BooleanField(verbose_name="Estado del producto", default=False)

    class Meta:
        verbose_name = "Analisis de Datos"
        verbose_name_plural = "Analisis de Datos"

    #Este es para que valor se muestre en la lista, sino semuestra un objects Productos(1)
    def __str__(self):
        return "{}".format(self.nombre_producto)

