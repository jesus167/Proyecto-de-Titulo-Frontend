from django.urls import path

from Home import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import logout

urlpatterns = [
    path('', views.home, name='Home'),
    path('pwd_restore/', views.recuperar_pwd, name='recuperar_pwd'),
    path('cerrar_sesion/', views.cerrar_sesion, name='Cerrar_sesion')
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)