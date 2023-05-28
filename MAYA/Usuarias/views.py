from django.shortcuts import redirect, render
import requests
from .forms import RegistrarUsuariaForm
from django.contrib import messages

url_usuaria = "http://127.0.0.1:8000/api/usuaria/"
url_perfil = "http://127.0.0.1:8000/api/perfil/"
perfiles = {}

def usuaria(request):
    return render(request, 'usuaria.html')

def registrarusuaria(request):
    global perfiles
    
    respuesta = requests.get(url_perfil)
    if respuesta.status_code == 200:
        perfil = respuesta.json()
        perfiles = {p["cod_perfil"]: p["perfil"] for p in perfil}
    else:
        print('Error en la búsqueda')

    form = RegistrarUsuariaForm(request.POST)
    if form.is_valid():
        u_registro = form.cleaned_data
        u_registro["nombre_perfil"] = perfiles.get(u_registro["perfil_cod_perfil"], "")
        
        response = requests.post(url_usuaria, u_registro)
        if response.status_code == 200:
            usuaria_creada = response.json()
            usuaria_creada["nombre_perfil"] = perfiles.get(usuaria_creada["perfil_cod_perfil"], "")
            return redirect('listarusuaria')  # Redirigir a la página de listar usuarias
        else:
            messages.error(request, 'Error al registrar usuaria')  # Mensaje de error
    else:
        form = RegistrarUsuariaForm()

    return render(request, 'registrarusuaria.html', {'form': form})

def listarusuaria(request):
    response = requests.get(url_usuaria)
    if response.status_code == 200:
        usuarias = response.json()
        for usuaria in usuarias:
            usuaria["nombre_perfil"] = perfiles.get(usuaria["perfil_cod_perfil"], "")
    else:
        usuarias = []

    context = {'usuarias': usuarias}
    return render(request, 'listarusuaria.html', context)
