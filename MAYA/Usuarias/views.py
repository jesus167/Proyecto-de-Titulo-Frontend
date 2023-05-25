from django.shortcuts import render
import requests
# Create your views here.

url_usuaria = "http://127.0.0.1:8000/api/usuaria/"
url_perfil= "http://127.0.0.1:8000/api/perfil/"

def usuaria(request):
    return render(request, 'usuaria/usuaria.html')

def registrar_usuaria(request):

    respuesta = requests.get('http://127.0.0.1:8000/api/perfil/')
    if respuesta.status_code == 200:
        perfil = respuesta.json()
        "perfil": perfil
    else:
        print('Error en la búsqueda')
    


    if request.method == 'POST':
        form = form(request.POST)
        u_registro = {
                "id_usuaria": request.POST['id'],
                "correo":request.POST['correo'], 
                "pwd":request.POST['clave'],
                "nombre":request.POST['nombre'], 
                "perfi_cod_perfil":request.POST['perfil']
                
            }
        response  = requests.post(url_usuaria, u_registro)
        if response.status_code == 200:
            print('Usuaria registrada')


    return render (request, 'Usuaria/registrar_usuaria.html', )

def listar_usuaria(request):
    data =  requests.get(url_usuaria)

    if data.status_code == 200:
        usuarias = data.json()
    context = {'usuaria': usuarias}


    return render (request, 'usuaria/listar_usuaria.html', context)


