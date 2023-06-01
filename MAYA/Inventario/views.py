import requests
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.


def inventario(request):
    return render(request, 'Inventario/inventario.html')

# LISTADO ARTÍCULOS
def articulo(request):
  respuesta = requests.get('http://127.0.0.1:8000/api/inventario/')
  if respuesta.status_code == 200:
    articulo = respuesta.json()
  else:
    print('Error en la búsqueda')
  contexto = {"articulo":articulo}
  return render(request,"Inventario/articulo.html", contexto)

# CREAR ARTÍCULO
def crearArticulo(request):
    respuesta1 = requests.get('http://127.0.0.1:8000/api/item/')
    if respuesta1.status_code == 200:
      item = respuesta1.json()
    else:
      print('Error en la búsqueda')
    respuesta2 = requests.get('http://127.0.0.1:8000/api/proveedora/')
    if respuesta2.status_code == 200:
      proveedora = respuesta2.json()
    else:
      print('Error en la búsqueda')
    respuesta3 = requests.get('http://127.0.0.1:8000/api/inventario/')
    if respuesta3.status_code == 200:
      articulo = respuesta3.json()
    else:
      print('Error en la búsqueda')
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            url = 'http://127.0.0.1:8000/api/inventario/'
            headers = {'Content-Type': 'application/json'}
            data = {
                'nom_art': form.cleaned_data['nom_art'],
                'item_cod_item': form.cleaned_data['item_cod_item'],
                'proveedora_cod_proveedora': form.cleaned_data['proveedora_cod_proveedora'],
            }
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 201:
                return redirect('Inventario/articulo.html')
    else:
        form = ArticuloForm()
    
    return render(request, 'Inventario/crearArticulo.html', {'form': form, 'item':item, 'proveedora':proveedora, 'articulo':articulo})

# ELIMINAR ARTÍCULO
def eliminarArticulo(request, id):
    print('Se eliminará el artículo', id)
    requests.delete('http://127.0.0.1:8000/api/inventario/{}'.format(id))
    return redirect('Inventario/articulo')

# REGISTRAR ENTRADA
def registrarEntrada(request):
  respuesta = requests.get('http://127.0.0.1:8000/api/inventario/')
  if respuesta.status_code == 200:
    articulo = respuesta.json()
  else:
      print('Error en la búsqueda')
  if request.method == 'POST':
      form = EntradaForm(request.POST)
      if form.is_valid():
          url = 'http://127.0.0.1:8000/api/entrada/'
          headers = {'Content-Type': 'application/json'}
          data = {
              'inventario_cod_art': form.cleaned_data['inventario_cod_art'],
              'cantidad': form.cleaned_data['cantidad'],
              'costo_unit': form.cleaned_data['costo_unit'],
              'descripcion': form.cleaned_data['descripcion'],
          }
          response = requests.post(url, headers=headers, json=data)
          if response.status_code == 201:
              return redirect('Inventario/articulo')
  else:
      form = EntradaForm() 
  return render(request, 'Inventario/registrarEntrada.html', {'form': form, 'articulo':articulo})

# REGISTRAR SALIDA
def registrarSalida(request):
  respuesta = requests.get('http://127.0.0.1:8000/api/inventario/')
  if respuesta.status_code == 200:
    articulo = respuesta.json()
  else:
      print('Error en la búsqueda')
  if request.method == 'POST':
      form = SalidaForm(request.POST)
      if form.is_valid():
          url = 'http://127.0.0.1:8000/api/salida/'
          headers = {'Content-Type': 'application/json'}
          data = {
              'inventario_cod_art': form.cleaned_data['inventario_cod_art'],
              'cantidad': form.cleaned_data['cantidad'],
              'descripcion': form.cleaned_data['descripcion'],
          }
          response = requests.post(url, headers=headers, json=data)
          if response.status_code == 201:
              return redirect('Inventario/articulo')
  else:
      form = EntradaForm() 
  return render(request, 'registrarSalida.html', {'form': form, 'articulo':articulo})

# LISTADO ÍTEMS
def item(request):
  respuesta = requests.get('http://127.0.0.1:8000/api/item/')
  if respuesta.status_code == 200:
    item = respuesta.json()
  else:
    print('Error en la búsqueda')
  contexto = {"item":item}
  return render(request,"Inventario/item.html", contexto)

# CREAR ÍTEM
def crearItem(request):
  respuesta = requests.get('http://127.0.0.1:8000/api/unidad/')
  if respuesta.status_code == 200:
    unidad = respuesta.json()
  else:
    print('Error en la búsqueda')

  if request.method == 'POST':
      form = ItemForm(request.POST)
      if form.is_valid():
          url = 'http://127.0.0.1:8000/api/item/'
          headers = {'Content-Type': 'application/json'}
          data = {
              'nom_item': form.cleaned_data['nom_item'],
              'categoria': form.cleaned_data['categoria'],
              'unidad_cod_unidad': form.cleaned_data['unidad_cod_unidad'],
              'cant_item': form.cleaned_data['cant_item'],
              'costo_std': form.cleaned_data['costo_std'],
          }
          response = requests.post(url, headers=headers, json=data)
          if response.status_code == 201:
              return redirect('/item')
  else:
      form = ProveedoraForm() 
  return render(request, 'Inventario/crearItem.html', {'form': form, 'unidad':unidad})

# EDITAR ÍTEM
def editarItem(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        url = 'http://127.0.0.1:8000/api/item/{}/'.format(id)
        data = {}
        editados = ['nom_item', 'categoria', 'unidad_cod_unidad', 'cant_item', 'costo_std']

        for campo in editados:
            nuevo_valor = request.POST.get(campo)
            if nuevo_valor:
               data[campo] = nuevo_valor
 
        response = requests.patch(url, data=data)

        if response.status_code == 200:
            print('El ítem ha sido actualizado correctamente.')
        else:
            print('Error al actualizar el ítem.')

    return redirect('Inventario/item')

# ELIMINAR ÍTEM
def eliminarItem(request, id):
    print('Se eliminará el ítem', id)
    requests.delete('http://127.0.0.1:8000/api/item/{}'.format(id))
    return redirect('Inventario/item')

# LISTADO PROVEEDORAS
def proveedora(request):
  respuesta = requests.get('http://127.0.0.1:8000/api/proveedora/')
  if respuesta.status_code == 200:
    proveedora = respuesta.json()
  else:
    print('Error en la búsqueda')
  contexto = {"proveedora":proveedora}
  return render(request,"Inventario/proveedora.html", contexto)

# CREAR PROVEEDORA
def crearProveedora(request):
    if request.method == 'POST':
        form = ProveedoraForm(request.POST)
        if form.is_valid():
            url = 'http://127.0.0.1:8000/api/proveedora/'
            headers = {'Content-Type': 'application/json'}
            data = {
                'nom_proveedora': form.cleaned_data['nom_proveedora'],
                'nom_contacto': form.cleaned_data['nom_contacto'],
                'correo': form.cleaned_data['correo'],
                'tel': form.cleaned_data['tel'],
                'calle': form.cleaned_data['calle'],
                'numero': form.cleaned_data['numero'],
                'complemento': form.cleaned_data['complemento'],
                'comuna_cod_comuna': 295,
                'pais_cod_pais': 44,
            }
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 201:
                return redirect('proveedora')
    else:
        form = ProveedoraForm()
    
    return render(request, 'Inventario/crearProveedora.html', {'form': form})

# EDITAR PROVEEDORA
def editarProveedora(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        url = 'http://127.0.0.1:8000/api/proveedora/{}/'.format(id)
        data = {}

        editados = ['nom_proveedora', 'nom_contacto', 'correo', 'tel', 'calle', 'numero', 'complemento']

        for campo in editados:
            nuevo_valor = request.POST.get(campo)
            if nuevo_valor:
               data[campo] = nuevo_valor
 
        response = requests.patch(url, data=data)

        if response.status_code == 200:
            print('La proveedora ha sido actualizada correctamente.')
        else:
            print('Error al actualizar la proveedora.')

    return redirect('Inventario/proveedora')

# ELIMINAR PROVEEDORA
def eliminarProveedora(request, id):
    print('Se eliminará la proveedora', id)
    requests.delete('http://127.0.0.1:8000/api/proveedora/{}'.format(id))
    return redirect('Inventario/proveedora')


