from django.urls import path

from Pedidos import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('', views.pedidos, name='Pedidos'),
    path('pedido/', views.pedido, name="pedido"),
    path('crearPedido/', views.crearPedido, name="crearPedido"),
    path('eliminarPedido/<id>', views.eliminarPedido, name="eliminarPedido"),

    path('registrarDetallePedido/', views.registrarDetallePedido, name="registrarDetallePedido"),
    path('asignarUsuaria/', views.asignarUsuaria, name="asignarUsuaria"),
    path('actualizarEstado/', views.actualizarEstado, name="actualizarEstado"),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)