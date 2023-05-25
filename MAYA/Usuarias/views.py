from django.shortcuts import render
import requests
# Create your views here.

url_usuaria = "http://127.0.0.1:8000/api/usuaria/"
url_perfil= "http://127.0.0.1:8000/api/perfil/"
perfiles = {}

def usuaria(request):
    return render(request, 'usuaria/usuaria.html')

def registrar_usuaria(request):

    respuesta = requests.get('http://127.0.0.1:8000/api/perfil/')
    if respuesta.status_code == 200:
        perfil = respuesta.json()
        perfiles = {p["cod_perfil"]: p["perfil"] for p in perfil}
    else:
        print('Error en la búsqueda')


    if request.method == 'POST':
        form = form(request.POST)
        u_registro = {
    "id_usuaria": request.POST['id'],
    "correo": request.POST['correo'], 
    "pwd": request.POST['clave'],
    "nombre": request.POST['nombre'], 
    "perfil_cod_perfil": request.POST['perfil']
}

# Asignar el nombre del perfil al diccionario de registro
    u_registro["nombre_perfil"] = perfiles.get(u_registro["perfil_cod_perfil"], "")

    response  = requests.post(url_usuaria, u_registro)
    if response.status_code == 200:
            print('Usuaria registrada')


    return render (request, 'usuaria/registrar_usuaria.html', )

def listar_usuaria(request):
    data = requests.get(url_usuaria)
    if data.status_code == 200:
        usuarias = data.json()
    for usuaria in usuarias:
        usuaria["nombre_perfil"] = perfiles.get(usuaria["perfil_cod_perfil"], "")
    context = {'usuarias': usuarias}
    return render (request, 'usuaria/listar_usuaria.html', context)


