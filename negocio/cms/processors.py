from .models import Inicio_banner, Inicio_titulo, Inicio_circulos, Inicio_cards, Inicio_foto_final, Footer, Productos_list, quiero_comprar

def Traer_Banner(request):
    Banners =Inicio_banner.objects.filter(activado=True)
    Titulo = Inicio_titulo.objects.filter(activado=True)
    Circulos = Inicio_circulos.objects.filter(activado=True)
    Cards = Inicio_cards.objects.filter(activado=True)
    Foto_final = Inicio_foto_final.objects.filter(activado=True)
    footer = Footer.objects.filter(activado=True)
    productos_list = Productos_list.objects.filter(activado=True)
    Quiero_comprar = quiero_comprar.objects.filter(activado=True)

    if Banners.count() > 0:
        Banners=Banners[Banners.count()-1]
    else:
        Banners=None

    if Titulo.count() > 0:
        Titulo = Titulo[Titulo.count() - 1]
    else:
        Titulo = None

    if Circulos.count() > 0:
        Circulos = Circulos[Circulos.count() - 1]
    else:
        Circulos = None

    if Cards.count() > 0:
        Cards = Cards[Cards.count() - 1]
    else:
        Cards = None

    if Foto_final.count() > 0:
        Foto_final = Foto_final[Foto_final.count() - 1]
    else:
        Foto_final = None

    if footer.count() > 0:
        footer = footer[footer.count() - 1]
    else:
        footer = None

    if productos_list.count() > 0:
        productos_list = productos_list[productos_list.count() - 1]
    else:
        productos_list = None

    if Quiero_comprar.count() > 0:
        Quiero_comprar = Quiero_comprar[Quiero_comprar.count() - 1]
    else:
        Quiero_comprar = None

    return {'Banners':Banners,'Titulo':Titulo,'Circulos':Circulos,'Cards':Cards,'Foto_final':Foto_final,'footer':footer,'productos_list':productos_list, 'Quiero_comprar':Quiero_comprar,}