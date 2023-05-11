from django.urls import path
from Login import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name='Login'),
    path('registro/', views.registro, name='Registro'),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)