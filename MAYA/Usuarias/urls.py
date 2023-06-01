from django.urls import path

from Usuarias import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.usuarias, name='Usuarias'),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)