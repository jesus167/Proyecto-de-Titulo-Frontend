import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PwdRestore

# Create your views here.
url_usuarias = 'http://127.0.0.1:8000/api/usuaria/'
url_restaurar_pwd = 'http://127.0.0.1:8000/api/cambioPwd/'
url_cerrar_sesion = 'http://127.0.0.1:8000/api/cierreSesion/'

# @login_required
def home(request):
    user =  requests.get(url_usuarias)
    if user.status_code == 200:
        user.json()
    contexto = {
        'usuaria': user
    }
    return render(request, 'Home/index.html', contexto)


def recuperar_pwd(request):
    msje = ""
    if request.method == 'POST':
        form = PwdRestore(request.POST)
        if form.is_valid():
            correo = request.POST['correo']
            new_pass = request.POST['new_pass']
            password = request.POST['password']
        payload = {
            "correo":correo,
            "newPwd":new_pass, 
            "pwd":password
        }
        cambio_pwd = requests.patch(url_restaurar_pwd, json = payload)
        if cambio_pwd.status_code == 200:
            msje = "Cambio de contraseña realizado ok"
            return redirect('Home')
        else:
            msje = "Datos inválidos"

    contexto = {"msje":msje}

    return render(request, 'Home/pwd_restore.html', contexto)

def cerrar_sesion(request):
    print('Hola')
    if request.method == 'POST':
        correo = 'ogutierrespinosa@gmail.com'
        canal = 1
        logout = {
            "correo": correo,
            "canal" : canal
        }
        data = requests.post(url_cerrar_sesion, json = logout)
        if data.status_code == 200:

            return redirect('Login')
        else:
            print("no es posible cerrar sesión")
        return redirect('Home')
    
    