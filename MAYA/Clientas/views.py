import requests
from django.shortcuts import render

url_clienta = "http://127.0.0.1:8000/api/clienta/"
url_pais= "http://127.0.0.1:8000/api/pais/"
url_region= "http://127.0.0.1:8000/api/region/"
url_comuna= "http://127.0.0.1:8000/api/comuna/"


def clientas(request):
    return render(request, 'Clientas/clientas.html')

def registro_clientas(request):

    respuesta = requests.get('http://127.0.0.1:8000/api/pais/')
    if respuesta.status_code == 200:
        paises = respuesta.json()
    else:
        print('Error en la búsqueda')
    

    respuesta = requests.get('http://127.0.0.1:8000/api/region/')
    if respuesta.status_code == 200:
        region = respuesta.json()
    else:
        print('Error en la búsqueda')
    

    respuesta = requests.get('http://127.0.0.1:8000/api/comuna/')
    if respuesta.status_code == 200:
        comunas = respuesta.json()
    else:
        print('Error en la búsqueda')
    context = {"comunas":comunas,
               "region": region,
               "paises": paises}



    if request.method == 'POST':
        form = form(request.POST)
        registro = {
                "rut_clienta": request.POST['rut'],
                "dv_clienta":request.POST['DV'], 
                "tipo_clienta":request.POST['tipo_clienta'],
                "nombre":request.POST['nombre'], 
                "apellido":request.POST['apellido'], 
                "nom_fantasia":request.POST['nombre_fantasia'],
                "rep_legal_cod_rep_legal":request.POST['representante'],
                "correo":request.POST['correo'],
                "tel": request.POST['telefono'],
                "pais_cod_pais": request.POST['rut'],
                "region_cod_pais":request.POST['rut'],
                "comuna_cod_comuna":request.POST['rut'],
                "calle":request.POST['direccion'],
                "numero":request.POST['numero'],
                "complemento":request.POST['Complemento'], 
                "giro":request.POST['giro'] 
            }
        response  = requests.post(url_clienta, registro)
        if response.status_code == 200:
            print('Clienta registrada')


    return render (request, 'Clientas/registro_clientas.html', context)

def listar_clientas(request):
    data =  requests.get(url_clienta)

    if data.status_code == 200:
        clientas = data.json()
    context = {'clientas': clientas}

    return render (request, 'Clientas/listar_clientas.html', context)


