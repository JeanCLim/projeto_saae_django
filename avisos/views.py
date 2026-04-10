from django.shortcuts import render
from .models import AvisoFaltaDagua

def lista_avisos(request):
    # Buscamos todos os avisos que NÃO são rascunho, ordenando pelos mais recentes
    avisos = AvisoFaltaDagua.objects.exclude(status='RASCUNHO').order_by('-data_criacao')
    
    return render(request, 'avisos/lista.html', {'avisos': avisos})