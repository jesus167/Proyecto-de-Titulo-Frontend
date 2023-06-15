import requests, json
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.


def pedidos(request):
    return render(request, 'Pedidos/pedidos.html')

#==============================   
# MÓDULO 4: PEDIDOS
#==============================

# LISTADO DE PEDIDOS Y DETALLE
def pedido(request):
    respuesta = requests.get('http://127.0.0.1:8000/api/pedido/')
    if respuesta.status_code == 200:
        pedido = respuesta.json()
    else:
        print('Error en la búsqueda de pedidos')

    respuesta2 = requests.get('http://127.0.0.1:8000/api/estadopedido/')
    if respuesta2.status_code == 200:
        estado = respuesta2.json()
    else:
        print('Error en la búsqueda de estados de pedidos')

    respuesta3 = requests.get('http://127.0.0.1:8000/api/usuaria/')
    if respuesta3.status_code == 200:
        usuaria = respuesta3.json()
    else:
        print('Error en la búsqueda de usuarias')

    respuesta4 = requests.get('http://127.0.0.1:8000/api/clienta/')
    if respuesta4.status_code == 200:
        clienta = respuesta4.json()
    else:
        print('Error en la búsqueda de clientas')

    respuesta5 = requests.get('http://127.0.0.1:8000/api/detallepedido/')
    if respuesta5.status_code == 200:
        detallepedido = respuesta5.json()
    else:
        print('Error en la búsqueda de detalle de pedidos')

    respuesta6 = requests.get('http://127.0.0.1:8000/api/unidad/')
    if respuesta6.status_code == 200:
        unidad = respuesta6.json()
    else:
        print('Error en la búsqueda de unidades')

    respuesta7 = requests.get('http://127.0.0.1:8000/api/item/')
    if respuesta7.status_code == 200:
        item = respuesta7.json()
    else:
        print('Error en la búsqueda de ítems')

    respuesta8 = requests.get('http://127.0.0.1:8000/api/ft/')
    if respuesta8.status_code == 200:
        ft = respuesta8.json()
    else:
        print('Error en la búsqueda de fichas técnicas')

    respuesta9 = requests.get('http://127.0.0.1:8000/api/comuna/')
    if respuesta9.status_code == 200:
        comuna = respuesta9.json()
    else:
        print('Error en la búsqueda de fichas técnicas')

    contexto = {'pedido':pedido, 'estado':estado, 'usuaria':usuaria, 'clienta':clienta, 'detallepedido':detallepedido, 'unidad':unidad, 'item':item, 'ft':ft, 'comuna':comuna}
    return render(request, "Pedidos/pedido.html", contexto)

# CREAR PEDIDO
def crearPedido(request):
    
    respuesta = requests.get('http://127.0.0.1:8000/api/clienta/')
    if respuesta.status_code == 200:
        clienta = respuesta.json()
    else:
        print('Error en la búsqueda de clientas')

    respuesta1 = requests.get('http://127.0.0.1:8000/api/usuaria/')
    if respuesta1.status_code == 200:
        usuaria = respuesta1.json()
    else:
        print('Error en la búsqueda de usuarias')

    respuesta3 = requests.get('http://127.0.0.1:8000/api/pedido/')
    if respuesta3.status_code == 200:
        pedido = respuesta3.json()
    else:
        print('Error en la búsqueda de pedidos')
    respuesta4 = requests.get('http://127.0.0.1:8000/api/item/')
    if respuesta4.status_code == 200:
        item = respuesta4.json()
    else:
        print('Error en la búsqueda de ítems')

    respuesta5 = requests.get('http://127.0.0.1:8000/api/ft/')
    if respuesta5.status_code == 200:
        ft = respuesta5.json()
    else:
        print('Error en la búsqueda de fichas técnicas')

    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            url = 'http://127.0.0.1:8000/api/pedido/'
            headers = {'Content-Type': 'application/json'}
            data = {
                'fecha_compromiso': form.cleaned_data['fecha_compromiso'].strftime('%Y-%m-%d'),
                'clienta_cod_clienta': form.cleaned_data['clienta_cod_clienta'],
            }
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 201:
                return redirect('pedido')
    else:
        form = PedidoForm()
    
    contexto = {'form': form, 'clienta': clienta, 'usuaria':usuaria, 'pedido':pedido, 'item':item, 'ft':ft}
    return render(request, 'Pedidos/crearPedido.html', contexto)

# REGISTRAR DETALLE DE PEDIDO
def registrarDetallePedido(request):
    msje = None
    if request.method == 'POST':
        form = DetallePedidoForm(request.POST)
        categoria = request.POST['categoria']
        if categoria == '1':
            ft_cod_ft = None
            item_cod_item = form['item_cod_item'].value()
        else:
            item_cod_item = None
            ft_cod_ft = form['ft_cod_ft'].value()

        if form.is_valid():
            url = 'http://127.0.0.1:8000/api/detallepedido/'
            headers = {'Content-Type': 'application/json'}
            data = {
                'pedido_cod_pedido': form.cleaned_data['pedido_cod_pedido'],
                'categoria': form.cleaned_data['categoria'],
                'item_cod_item': item_cod_item,
                'ft_cod_ft': ft_cod_ft,
                'cantidad': form.cleaned_data['cantidad'],
            }
            print(data)
            json_data = json.dumps(data)
            response = requests.post(url, headers=headers, data=json_data)
            if response.status_code == 201:
                msje = 'Ítem registrado'
                contexto = {'msje':msje}
                return redirect('crearPedido', contexto)
    else:
        form = DetallePedidoForm()
    contexto = {'form': form, 'msje':msje}
    return render(request, 'Pedidos/crearPedido.html', contexto)

# ELIMINAR PEDIDO
def eliminarPedido(request, id):
    print('Se eliminará el pedido', id)
    requests.delete('http://127.0.0.1:8000/api/pedido/{}'.format(id))
    return redirect('pedido')

# ASIGNAR USUARIA
def asignarUsuaria(request):
    id_usuaria = 0
    cod_pedido = 0
    try:
        id_usuaria = request.POST.get("id_usuaria")
        cod_pedido = request.POST.get("cod_pedido")
    except:
        print("No pasa nada")

    payload = {
        "id_usuaria":id_usuaria,
        "cod_pedido":cod_pedido
    }
    respuesta = requests.patch('http://127.0.0.1:8000/api/asignarUsuaria/', json = payload)
    data = respuesta.json()

    if respuesta.status_code == 200:
        msje1 = '¡Todo ok! '
        msje2 = data
    elif respuesta.status_code == 409:
        msje1 = 'USUARIA NO ASIGNADA '
        msje2 = 'No hay suficiente stock de: '+', '.join(item['nom_item'] for item in data)
    else:
        msje1 = 'USUARIA NO ASIGNADA '
        msje2 = data

    redirect_url = 'pedido?msje1={}&msje2={}'.format(msje1, msje2)
    return redirect(redirect_url)

    # ACTUALIZAR ESTADO
def actualizarEstado(request):
    cod_pedido = 0
    new_estado = 0
    try:
        cod_pedido = request.POST.get("cod_pedido")
        new_estado = request.POST.get("new_estado")
        print(new_estado)
    except:
        print("No pasa nada")

    payload = {
        "cod_pedido":cod_pedido,
        "new_estado":new_estado
    }
    print(payload)
    respuesta = requests.post('http://127.0.0.1:8000/api/actualizarEstadoPedido/', json = payload)
    data = respuesta.json()

    if respuesta.status_code == 200:
        msje1 = 'Pedido actualizado '
        msje2 = data
    elif respuesta.status_code == 400:
        msje1 = 'ESTADO NO ACTUALIZADO '
        msje2 = data
    else:
        msje1 = 'ERROR '
        msje2 = 'Pida ayuda'

    redirect_url = 'pedido?msje1={}&msje2={}'.format(msje1, msje2)
    return redirect(redirect_url)
