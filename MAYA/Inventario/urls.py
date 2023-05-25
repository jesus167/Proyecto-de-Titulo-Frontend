from django.urls import path

from Inventario import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inventario, name='Inventario'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)