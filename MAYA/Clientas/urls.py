from django.urls import path

from Clientas import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.clientas, name='Clientas'),
    path('registro/', views.registro_clientas, name='registro'),
    path('listar/', views.listar_clientas, name='listar'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)