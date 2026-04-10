from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('avisos.urls')), # Isso conecta o site principal ao seu app de avisos
]