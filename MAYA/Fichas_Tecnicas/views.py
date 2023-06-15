import requests
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .forms import *


#==============================   
# MÓDULO 3: FICHAS TÉCNICAS
#==============================

# PANTALLA INICIAL DEL MÓDULO

def fichas_tecnicas(request):
    return render(request, 'Fichas_Tecnicas/fichas_tecnicas.html')

def ft(request):
    respuesta = requests.get('http://127.0.0.1:8000/api/ft/')
    if respuesta.status_code == 200:
        ft = respuesta.json()
    else:
        print('Error en la búsqueda')

    respuesta1 = requests.get('http://127.0.0.1:8000/api/detalleingrediente/')
    if respuesta1.status_code == 200:
        det_ingr = respuesta1.json()
    else:
        print('Error en la búsqueda de detalle de ingredientes')

    respuesta2 = requests.get('http://127.0.0.1:8000/api/detallepreparacion/')
    if respuesta2.status_code == 200:
        det_prep = respuesta2.json()
    else:
        print('Error en la búsqueda de detalle de preparación')

    respuesta3 = requests.get('http://127.0.0.1:8000/api/item/')
    if respuesta3.status_code == 200:
        item = respuesta3.json()
    else:
        print('Error en la búsqueda de ítems')
    
    respuesta4 = requests.get('http://127.0.0.1:8000/api/unidad/')
    if respuesta4.status_code == 200:
        unidad = respuesta4.json()
    else:
        print('Error en la búsqueda de unidades')

    contexto = {'ft':ft, 'det_ingr':det_ingr, 'det_prep':det_prep, 'item':item, 'unidad':unidad}
    return render(request,"Fichas_Tecnicas/fichas_tecnicas.html", contexto)

# CREAR FT
def crearFt(request):
    
    respuesta = requests.get('http://127.0.0.1:8000/api/item/')
    if respuesta.status_code == 200:
        item = respuesta.json()
    else:
        print('Error en la búsqueda de ítems')

    respuesta1 = requests.get('http://127.0.0.1:8000/api/ft/')
    if respuesta1.status_code == 200:
        ft = respuesta1.json()
    else:
        print('Error en la búsqueda de fichas técnicas')

    if request.method == 'POST':
        form = FtForm(request.POST, request.FILES)
        if form.is_valid():
            nom_ft = form.cleaned_data['nom_ft']
            rendimiento = form.cleaned_data['rendimiento']
            observacion = form.cleaned_data['observacion']
            costo_tot = 0

            data = {
                'nom_ft': nom_ft,
                'rendimiento': rendimiento,
                'observacion': observacion,
                'costo_tot': costo_tot
            }
            files = {}
            if 'img_ft' in request.FILES:
                files['img_ft'] = request.FILES['img_ft']

            response = requests.post('http://127.0.0.1:8000/api/ft/', data=data, files=files)

            if response.status_code == 201:
                return redirect('ft')
            else:
                form.add_error(None, 'Error al enviar los datos')
    else:
        form = FtForm()
    contexto = {'form': form, 'ft':ft, 'item':item}
    return render(request, 'Fichas_Tecnicas/crearFt.html', contexto)

# ELIMINAR FICHA TÉCNICA
def eliminarFt(request, id):
    print('Se eliminará la ficha técnica', id)
    requests.delete('http://127.0.0.1:8000/api/ft/{}'.format(id))
    return redirect('ft')

# REGISTRAR INGREDIENTES
def registrarIngrediente(request):

    if request.method == 'POST':
        form = DetalleIngredienteForm(request.POST)
        if form.is_valid():
            url = 'http://127.0.0.1:8000/api/detalleingrediente/'
            headers = {'Content-Type': 'application/json'}
            data = {
                'ft_cod_ft': form.cleaned_data['ft_cod_ft'],
                'item_cod_item': form.cleaned_data['item_cod_item'],
                'cantidad': form.cleaned_data['cantidad'],
            }
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 201:
                return redirect('crearFt')
    else:
        form = DetalleIngredienteForm()
    contexto = {'form': form}
    return render(request, 'Fichas_Tecnicas/crearFt.html', contexto)

# REGISTRAR PREPARACIÓN
def registrarPreparacion(request):

    if request.method == 'POST':
        form = DetallePreparacionForm(request.POST)
        if form.is_valid():
            url = 'http://127.0.0.1:8000/api/detallepreparacion/'
            headers = {'Content-Type': 'application/json'}
            data = {
                'ft_cod_ft': form.cleaned_data['ft_cod_ft'],
                'instruccion': form.cleaned_data['instruccion'],
            }
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 201:
                return redirect('crearFt')
    else:
        form = DetallePreparacionForm()
    contexto = {'form': form}
    return render(request, 'Ficha_Tecnica/crearFt.html', contexto)

# SIMULAR FICHA TÉCNICA
def simularFt(request):
    ft_cod_ft = request.POST.get('ft_cod_ft')
    personas = int(request.POST.get('personas'))

    print("Ficha técnica code:", ft_cod_ft)
    print("Cantidad de personas:", personas)

    url = f"http://127.0.0.1:8000/api/simularFt/?cod_ft={ft_cod_ft}&personas={personas}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        ingredientes_simulados = data['ingredientes_simulados']
        ft_simulada = data['ft_simulada']
        print("Ingredientes simulados:", ingredientes_simulados)
        print("Ficha técnica simulada:", ft_simulada)
    else:
        print("Error en la simulación", response.status_code)

    response_data = {
        'ingredientes_simulados': ingredientes_simulados,
        'ft_simulada': ft_simulada
    }
    return JsonResponse(response_data)
