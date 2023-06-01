from django.urls import path

from Inventario import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inventario, name='Inventario'),
    path('articulo/', views.articulo, name="articulo"),
    path('crearArticulo/', views.crearArticulo, name="crearArticulo"),
    path('eliminarArticulo/<id>', views.eliminarArticulo, name="eliminarArticulo"),

    path('registrarEntrada/', views.registrarEntrada, name="registrarEntrada"),
    path('registrarSalida/', views.registrarSalida, name="registrarSalida"),

    path('item/', views.item, name="item"),
    path('crearItem/', views.crearItem, name="crearItem"),
    path('editarItem', views.editarItem, name="editarItem"),
    path('eliminarItem/<id>', views.eliminarItem, name="eliminarItem"),

    path('proveedora/', views.proveedora, name="proveedora"),
    path('crearProveedora/', views.crearProveedora, name="crearProveedora"),
    path('editarProveedora', views.editarProveedora, name="editarProveedora"),
    path('eliminarProveedora/<id>', views.eliminarProveedora, name="eliminarProveedora"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)