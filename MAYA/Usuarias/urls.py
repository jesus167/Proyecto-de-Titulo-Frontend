from django.urls import path
from Usuarias import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.usuaria, name='usuaria'),
    path('registrar_usuaria/', views.registro_usuaria, name='registrar_usuaria'),
    path('listar_usuaria/', views.listar_usuaria, name='listar_usuaria'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)