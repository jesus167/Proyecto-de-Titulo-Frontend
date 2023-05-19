import requests
from django.shortcuts import render

url_clienta = "http://127.0.0.1:8000/api/clienta/"
url_pais= "http://127.0.0.1:8000/api/pais/"
url_region= "http://127.0.0.1:8000/api/region/"
url_comuna= "http://127.0.0.1:8000/api/comuna/"


def paises(request):
    respuesta = requests.get('http://127.0.0.1:8000/api/pais/')
    if respuesta.status_code == 200:
        paises = respuesta.json()
    else:
        print('Error en la búsqueda')
    pais = {"paises":paises}
    return render(request,'Clientas/registro_clientas.html', pais)

def region(request):
    respuesta = requests.get('http://127.0.0.1:8000/api/region/')
    if respuesta.status_code == 200:
        region = respuesta.json()
    else:
        print('Error en la búsqueda')
    regiones = {"paises":region}
    return render(request,'Clientas/registro_clientas.html', regiones)

def comuna(request):
    respuesta = requests.get('http://127.0.0.1:8000/api/comuna/')
    if respuesta.status_code == 200:
        comunas = respuesta.json()
    else:
        print('Error en la búsqueda')
    comuna = {"paises":comunas}
    return render(request,'Clientas/registro_clientas.html', comuna)

def clientas(request):
    return render (request, 'Clientas/clientas.html')


def registro_clientas(request):




    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            registro = {
                "rut_clienta": request.POST['rut'],
                "dv_clienta":request.POST['rut'], 
                "tipo_clienta":request.POST['rut'],
                "nombre":request.POST['rut'], 
                "apellido":request.POST['rut'], 
                "nom_fantasia":request.POST['rut'],
                "rep_legal_cod_rep_legal":request.POST['rut'],
                "correo":request.POST['rut'],
                "tel": request.POST['rut'],
                "pais_cod_pais": request.POST['rut'],
                "region_cod_pais":request.POST['rut'],
                "comuna_cod_comuna":request.POST['rut'],
                "calle":request.POST['rut'],
                "numero":request.POST['rut'],
                "complemento":request.POST['rut'], 
                "giro":request.POST['rut'] 
            }


    return render (request, 'Clientas/registro_clientas.html')

def listar_clientas(request):
    data =  requests.get(url_clienta)

    if data.status_code == 200:
        data.json()
    context = data

    return render (request, 'Clientas/listar_clientas.html', {'context': context})


