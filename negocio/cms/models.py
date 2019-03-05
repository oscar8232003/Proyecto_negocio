from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Inicio_banner(models.Model):
    banner1 = models.ImageField(verbose_name="Banner 1", upload_to='core/banner/', default="core/banner/carousel1.jpg")
    banner_titulo1=models.CharField(verbose_name="Titulo del banner 1", max_length=100, default="Titulo 1")
    banner_subtitulo1= models.CharField(verbose_name="Subtitulo del banner 1", max_length=100, default="Mensaje 1")

    banner2 = models.ImageField(verbose_name="Banner 2", upload_to='core/banner/', default="core/banner/carousel2.jpg")
    banner_titulo2= models.CharField(verbose_name="Titulo del banner 2", max_length=100,  default="Titulo 2")
    banner_subtitulo2 = models.CharField(verbose_name="Subtitulo del banner 2", max_length=100, default="Mensaje 2")

    banner3 = models.ImageField(verbose_name="Banner 3", upload_to='core/banner/', default="core/banner/carousel3.jpg")
    banner_titulo3= models.CharField(verbose_name="Titulo del banner 3", max_length=100,  default="Titulo 3")
    banner_subtitulo3 = models.CharField(verbose_name="Subtitulo del banner 3", max_length=100, default="Mensaje 3")

    activado = models.BooleanField(verbose_name="Conjunto Activado", default=False)

    class Meta:
        verbose_name="Inicio Banner"
        verbose_name_plural = "Inicio Banners"
        ordering = ['id']

    def __str__(self):
        return "Conjunto de banner n° {}".format(self.id)


class Inicio_titulo(models.Model):
    titulo_principal = models.CharField(verbose_name="Titulo Principal", max_length=200, default="Bienvenido al local de la Sra. Ines")
    subtitulo_principal = models.CharField(verbose_name="Subtitulo Principal", max_length=200, default="Donde siempre tenemos de todo un poco")

    activado = models.BooleanField(verbose_name="Conjunto Activado", default=False)

    class Meta:
        verbose_name = "Titulo de Inicio"
        verbose_name_plural = "Titulo de Inicio"

    def __str__(self):
        return "Conjunto de Titulo n° {}".format(self.id)


class Inicio_circulos(models.Model):
    circulo1_titulo = models.CharField(verbose_name="Titulo de 1° Circulo", max_length=100, default="Siempre Fresco")
    circulo1_contenido = RichTextField(verbose_name="Contenido de 1° Circulo", max_length=200, null=True, blank=True)

    circulo2_titulo = models.CharField(verbose_name="Titulo de 2° Circulo", max_length=100, default="Mejores Precios")
    circulo2_contenido = RichTextField(verbose_name="Contenido de 2° Circulo", max_length=200, null=True, blank=True)

    circulo3_titulo = models.CharField(verbose_name="Titulo de 3° Circulo", max_length=100, default="Buena Calidad")
    circulo3_contenido = RichTextField(verbose_name="Contenido de 3° Circulo", max_length=200, null=True, blank=True)

    activado = models.BooleanField(verbose_name="Conjunto Activado", default=False)


    class Meta:
        verbose_name = "Conjunto de Circulo"
        verbose_name_plural = "Conjunto de Circulos"

    def __str__(self):
        return "Conjunto de Circulos n° {}".format(self.id)

class Inicio_cards(models.Model):
    titulo_cards = models.CharField(verbose_name="Titulo de las Cards", max_length=100, default="Creemos en")

    img_card1 = models.ImageField(verbose_name="Imagen de Card 1", upload_to='core/index/', default="core/index/muestra1.JPG")
    titulo_card1 = models.CharField(verbose_name="Titulo de Card 1", max_length=200, default="Card Title 1")
    contenido_card1 = RichTextField(verbose_name="Contenido de Card 1", null=True, blank=True)

    img_card2 = models.ImageField(verbose_name="Imagen de Card 2", upload_to='core/index/', default="core/index/muestra2.JPG")
    titulo_card2 = models.CharField(verbose_name="Titulo de Card 2", max_length=200, default="Card Title 2")
    contenido_card2 = RichTextField(verbose_name="Contenido de Card 2", null=True, blank=True)

    img_card3 = models.ImageField(verbose_name="Imagen de Card 3", upload_to='core/index/', default="core/index/muestra3.JPG")
    titulo_card3 = models.CharField(verbose_name="Titulo de Card 3", max_length=200, default="Card Title 3")
    contenido_card3 = RichTextField(verbose_name="Contenido de Card 3", null=True, blank=True)

    img_card4 = models.ImageField(verbose_name="Imagen de Card 4", upload_to='core/index/', default="core/index/muestra4.png")
    titulo_card4 = models.CharField(verbose_name="Titulo de Card 4", max_length=200, default="Card Title 4")
    contenido_card4 = RichTextField(verbose_name="Contenido de Card 4", null=True, blank=True)

    activado = models.BooleanField(verbose_name="Conjunto Activado", default=False)

    class Meta:
        verbose_name = "Conjunto de Card"
        verbose_name_plural = "Conjunto de Cards"

    def __str__(self):
        return "Conjunto de Cards n° {}".format(self.id)


class Inicio_foto_final(models.Model):
    img_foto_final = models.ImageField(verbose_name="Imagen de la foto del final", upload_to='core/index/', default="core/index/imb-botom.JPG")
    titulo_foto_final = models.CharField(verbose_name="Titulo de la foto del final", max_length=200, default="Card Title Final Photo")
    contenido_foto_final = RichTextField(verbose_name="Contenido de la foto del final", null=True, blank=True)

    activado = models.BooleanField(verbose_name="Conjunto Activado", default=False)

    class Meta:
        verbose_name = "Conjunto de la Foto Final"
        verbose_name_plural = "Conjunto de la Foto Final"

    def __str__(self):
        return "Conjunto de la Foto Final n° {}".format(self.id)

class Footer(models.Model):
    direccion = models.CharField(verbose_name="Direccion", max_length=200, default="Jose Miguel Carrera 1997, Macul")
    contacto = models.CharField(verbose_name="Contacto", max_length=100, default="(02) 28232003")
    email = models.CharField(verbose_name="Email", max_length=100, default="oavr.18@gmail.com")

    activado = models.BooleanField(verbose_name="Conjunto Activado", default=False)

    class Meta:
        verbose_name = "Footer"
        verbose_name_plural = "Footer"

    def __str__(self):
        return "Conjunto Footer n° {}".format(self.id)

class Productos_list(models.Model):
    titulo_list = models.CharField(verbose_name="Titulo de Productos", max_length=200, default="Productos")
    subtitulo_list = models.CharField(verbose_name="Subtitulo de Productos", max_length=300, null=True, blank=True)

    activado = models.BooleanField(verbose_name="Conjunto Activado", default=False)

    class Meta:
        verbose_name = "Productos Listar"
        verbose_name_plural = "Productos Listar"

    def __str__(self):
        return "Conjunto Productos n° {}".format(self.id)

class quiero_comprar(models.Model):
    titulo = models.CharField(verbose_name="Titulo de Quiero comprar", max_length=200, default="¿Quieres comprar?")
    subtitulo = models.CharField(verbose_name="Subtitulo de Quiero comprar", max_length=300, default="Aqui te diremos como puedes comprar, donde nos ubicamos y los medios de forma de pago.")

    titulo_card1 = models.CharField(verbose_name="Titulo de 1° Card", max_length=200, default="Como comprar")
    contenido_card1 = RichTextField(verbose_name="Contenido de 1° Card", null=True, blank=True)

    titulo_card2 = models.CharField(verbose_name="Titulo de 2° Card", max_length=200, default="Donde nos ubicamos")
    contenido_card2 = RichTextField(verbose_name="Contenido de 2° Card", null=True, blank=True)

    titulo_card3 = models.CharField(verbose_name="Titulo de 3° Card", max_length=200, default="Medios de pago")
    contenido_card3 = RichTextField(verbose_name="Contenido de 3° Card", null=True, blank=True)

    activado = models.BooleanField(verbose_name="Conjunto Activado", default=False)

    class Meta:
        verbose_name = "Quiero Comprar"
        verbose_name_plural = "Quiero Comprar"

    def __str__(self):
        return "Conjunto Quiero Comprar n° {}".format(self.id)