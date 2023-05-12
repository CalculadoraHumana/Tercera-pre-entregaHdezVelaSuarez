from django.shortcuts import render
from .forms import MiModeloForm
from .models import MiModelo, SegundoModelo, TercerModelo

def lista_mi_modelo(request):
    objetos = MiModelo.objects.all()
    return render(request, 'mi_modelo_lista.html', {'objetos': objetos})

def lista_segundo_modelo(request):
    objetos = SegundoModelo.objects.all()
    return render(request, 'segundo_modelo_lista.html', {'objetos': objetos})

def lista_tercer_modelo(request):
    objetos = TercerModelo.objects.all()
    return render(request, 'tercer_modelo_lista.html', {'objetos': objetos})



# Create your views here.
