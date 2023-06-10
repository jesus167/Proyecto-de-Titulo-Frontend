import requests
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .forms import *

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
    
    respuesta = requests.get('http://127.0.0.1:8000/api/replegal/')
    if respuesta.status_code == 200:
        replegal = respuesta.json()
    else:
        print('Error en la búsqueda')
    context = {"comunas":comunas,
                "region": region,
                "paises": paises,
                "rep_legal":replegal
                }

    if request.method == 'POST':
        form = RegistroClientas(request.POST)
        if form.is_valid():
            headers = {'Content-Type': 'application/json'}
            data = {
                    'rut_clienta': form.cleaned_data['rut_clienta'],
                    'dv_clienta':form.cleaned_data['dv_clienta'], 
                    'tipo_clienta':form.cleaned_data['tipo_clienta'],
                    'nombre':form.cleaned_data['nombre'], 
                    'apellido':form.cleaned_data['apellido'], 
                    'nom_fantasia':form.cleaned_data['nom_fantasia'],
                    'rep_legal_cod_rep_legal':form.cleaned_data['rep_legal_cod_rep_legal'],
                    'correo':form.cleaned_data['correo'],
                    'tel': form.cleaned_data['tel'],
                    'pais_cod_pais':form.cleaned_data['pais_cod_pais'],
                    'comuna_cod_comuna':form.cleaned_data['comuna_cod_comuna'],
                    'calle':form.cleaned_data['calle'],
                    'numero':form.cleaned_data['numero'],
                    'complemento': form.cleaned_data['complemento'],
                    'giro':form.cleaned_data['giro'] 
                }
            response  = requests.post(url_clienta, headers=headers, json=data)
            if response.status_code == 201:
                print('Clienta registrada')
                return redirect('listar')
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

# Listar otros datos de la Clienta
def otrosDatos(request):
    msje = " "
    respuesta = requests.get(url_clienta)
    if respuesta.status_code == 200:
        clienta = respuesta.json()
    else:
        print('Error en la búsqueda')
    data_clienta = {"clienta":clienta}

    rep_legal = requests.get(url_rep_legal)
    if rep_legal.status_code == 200:
        rep_legal = rep_legal.json()
    else:
        msje= "No tiene representante legal"
    data_rep = {'rep_legal':rep_legal}

    return render(request, 'Clientas/otrosDatos.html', data_clienta, data_rep, msje)

# Ingresar representante legal Asociado a Clienta
def rep_legal(request):
    if request.method == 'POST':
        form = RepresentanteLegal(request.POST)
        if form.is_valid():
            headers = {'Content-Type': 'application/json'}
            data ={
                'rut_rep_legal': form.cleaned_data['rut_rep_legal'],
                'dv_rep_legal': form.cleaned_data['dv_rep_legal'],
                'nombre': form.cleaned_data['nombre'],
                'apellido': form.cleaned_data['apellido'],
                'correo': form.cleaned_data['correo'],
                'tel': form.cleaned_data['tel']
            }
            guardar_RL = requests.post(url_rep_legal, headers=headers, json=data)
            if guardar_RL.status_code == 201:
                return redirect('registro')
        else:
            
            form = RepresentanteLegal()

    return render(request, 'Clientas/rep_leg.html', {'form':form})


def editarClienta(request):
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
    
    respuesta = requests.get('http://127.0.0.1:8000/api/replegal/')
    if respuesta.status_code == 200:
        replegal = respuesta.json()
    else:
        print('Error en la búsqueda')
    context = {"comunas":comunas,
                "region": region,
                "paises": paises,
                "rep_legal":replegal
                }
    return render(request, 'Clientas/editarclienta.html', context)


