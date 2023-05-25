import requests
from django.db import models


# Create your models here.
# url = "http://127.0.0.1:8000/api/comuna/"

# data_comuna = requests.get(url)

# if data_comuna.status_code == 200:
#     data_comuna.json()

# comuna_diccionario = {
#     data_comuna.json()
# }


class Clienta(models.Model):
    rut_clienta = models.IntegerField(verbose_name= 'Rut')
    dv_clienta = models.CharField(max_length=1, verbose_name= 'Dv')
    tipo_clienta = models.IntegerField(verbose_name='Tipo de Clienta')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100,verbose_name='Apellido')
    nom_fantasia = models.CharField(max_length=100, verbose_name='Nombre de Fantasia')
    #rep_legal_cod_rep_legal = models.ForeignKey('RepLegal', models.DO_NOTHING, db_column='rep_legal_cod_rep_legal', blank=True, null=True)
    correo = models.EmailField(max_length=100, verbose_name='Correo')
    tel = models.IntegerField(verbose_name='Telefono de Contacto')
    # pais_cod_pais = models.CharField(choices= "", verbose_name='Comuna')
    # region_cod_pais = models.CharField(choices="", verbose_name='Region')
    # comuna_cod_comuna = models.CharField(choices="", verbose_name='Comuna')
    # calle = models.CharField(max_length=200, verbose_name='Dirección')
    numero = models.IntegerField(verbose_name='Número')
    complemento = models.CharField(max_length=10, verbose_name='Datos adicionales a la dirección')
    giro = models.CharField(max_length=200, verbose_name='Giro Empresa')


