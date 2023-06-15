import requests
from django.shortcuts import render


url_pedido = "http://127.0.0.1:8000/api/pedido/"
# Create your views here.


def ventas(request):

    response = requests.get(url_pedido)

    if response.status_code == 200:
        data = response.json()

    context =  {'data': data}
    return render(request, 'Ventas/ventas.html',context)