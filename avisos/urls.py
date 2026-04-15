from django.urls import path
from . import views

urlpatterns = [
    # Isso diz que a página inicial do app vai chamar a sua lista de avisos
    path('', views.lista_avisos, name='lista_avisos'), 
]