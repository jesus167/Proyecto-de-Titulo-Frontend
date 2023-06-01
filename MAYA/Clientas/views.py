import requests
from django.http.response import JsonResponse
from django.shortcuts import render
from .forms import RegistroClientas

url_clienta = "http://127.0.0.1:8000/api/clienta/"
url_pais= "http://127.0.0.1:8000/api/pais/"
url_region= "http://127.0.0.1:8000/api/region/"
url_comuna= "http://127.0.0.1:8000/api/comuna/"
url_rep_legal= "http://127.0.0.1:8000/api/replegal/"


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
        form = RegistroClientas(request.POST)
        if form.is_valid():

            # headers = {'Content-Type': 'application/json'}
            # data = {
            #     'nom_item': form.cleaned_data['nom_item'],
            #     'categoria': form.cleaned_data['categoria'],
            #     'unidad_cod_unidad': form.cleaned_data['unidad_cod_unidad'],
            #     'cant_item': form.cleaned_data['cant_item'],
            #     'costo_std': form.cleaned_data['costo_std'],
            # }
            rut = request.POST['RUT']
            dv= request.POST['DV']
            tipo_clienta = request.POST['tipo_clienta']
            nombre= request.POST['nombre']
            apellido= request.POST['apellido']
            nom_fantasia = request.POST['nombre_fantasia']
            rlegal = request.POST['representante'] 
            correo = request.POST['correo']
            tel = request.POST['telefono']
            pais = request.POST['pais']
            comuna = request.POST['comuna']
            direccion = request.POST['direccion']
            numero = request.POST['numero']
            complemento = request.POST['Complemento']
            giro = request.POST['giro'] 
            registro = {
                    "rut_clienta": rut,
                    "dv_clienta":dv, 
                    "tipo_clienta":tipo_clienta,
                    "nombre":nombre, 
                    "apellido":apellido, 
                    "nom_fantasia":nom_fantasia,
                    "rep_legal_cod_rep_legal":rlegal,
                    "correo":correo,
                    "tel": tel,
                    "pais_cod_pais": pais,
                    "comuna_cod_comuna":comuna,
                    "calle":direccion,
                    "numero":numero,
                    "complemento": complemento,
                    "giro":giro 
                }
            print(registro)
            response  = requests.post(url_clienta, registro)
            if response.status_code == 201:
                print('Clienta registrada')
            else:
                print(response.status_code)
                print('No se registra')
    return render (request, 'Clientas/registro_clientas.html', context)

#    Listado de Clientas

def listar_clientas(request):
    respuesta = requests.get(url_clienta)
    if respuesta.status_code == 200:
        clienta = respuesta.json()
    else:
        print('Error en la búsqueda')
    contexto = {"clienta":clienta}
    return render(request, 'Clientas/listar_clientas.html', contexto)

def otrosDatos(request):
    msje = " "
    respuesta = requests.get(url_clienta)
    if respuesta.status_code == 200:
        clienta = respuesta.json()
    else:
        print('Error en la búsqueda')
    contexto = {"clienta":clienta}

    rep_legal = requests.get(url_rep_legal)
    if rep_legal.status_code == 200:
        rep_legal.json()
    else:
        msje= "No tiene representante legal"
    data_rep = {'rep_legal':rep_legal}

    return render(request, 'Clientas/otrosDatos.html', contexto, data_rep, msje)






