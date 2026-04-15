from django.shortcuts import render
from .models import AvisoFaltaDagua  # Importando o seu banco de dados (Ajuste se o nome do modelo for diferente)

def lista_avisos(request):
    # Pega todos os avisos cadastrados no banco de dados
    avisos = AvisoFaltaDagua.objects.all() 
    
    # Envia os dados para a sua página HTML Neon
    return render(request, 'lista.html', {'avisos': avisos})