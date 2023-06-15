from django.urls import path

from Fichas_Tecnicas import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.fichas_tecnicas, name="Fichas Tecnicas"),
    path('ft/', views.ft, name='ft'),
    path('crearFt/', views.crearFt, name="crearFt"),
    path('eliminarFt/<id>', views.eliminarFt, name="eliminarFt"),
    path('simularFt/', views.simularFt, name="simularFt"),

    path('registrarIngrediente/', views.registrarIngrediente, name="registrarIngrediente"),
    path('registrarPreparacion/', views.registrarPreparacion, name="registrarPreparacion"),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)