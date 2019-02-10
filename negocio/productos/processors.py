from .models import Categorias

def Traer_Categorias(request):
    return {'Categorias':Categorias.objects.all()}